#!/usr/bin/env python
"""Reusable Scanpy workflow for 10x feature-barcode matrices.

This scaffold contains no study data or study-specific thresholds. Inspect the
QC figures and complete config/thresholds.csv before running filters.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import anndata as ad
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
from scipy import sparse


def read_csv(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError("Input table is empty: {}".format(path))
    return frame


def require_columns(frame: pd.DataFrame, required: set[str], label: str) -> None:
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError("{} missing columns: {}".format(label, sorted(missing)))


def load_matrix(row: pd.Series) -> ad.AnnData:
    matrix_dir = Path(str(row["matrix_dir"])).expanduser()
    if not matrix_dir.is_dir():
        raise FileNotFoundError("Matrix directory not found: {}".format(matrix_dir))
    x = sc.read_10x_mtx(
        matrix_dir, var_names="gene_symbols", make_unique=True, cache=False
    )
    x.var_names_make_unique()
    x.obs["sample_id"] = str(row["sample_id"])
    for col in ("group", "donor_id", "batch"):
        x.obs[col] = str(row.get(col, "unspecified"))
    return x


def annotate_genes(x: ad.AnnData) -> None:
    names = pd.Index(x.var_names.astype(str)).str.upper()
    x.var["mt"] = names.str.startswith("MT-")
    x.var["ribo"] = names.str.startswith(("RPS", "RPL"))


def calculate_qc(x: ad.AnnData) -> None:
    sc.pp.calculate_qc_metrics(
        x, qc_vars=["mt", "ribo"], percent_top=None, log1p=False, inplace=True
    )


def save_qc_plots(x: ad.AnnData, out: Path, tag: str) -> None:
    out.mkdir(parents=True, exist_ok=True)
    metrics = ["total_counts", "n_genes_by_counts", "pct_counts_mt", "pct_counts_ribo"]
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    for ax, metric in zip(axes.flat, metrics):
        ax.hist(x.obs[metric].dropna(), bins=50, color="#4C91B8", edgecolor="white")
        ax.set_title(metric.replace("_", " "))
        ax.set_ylabel("Cells")
        ax.set_xlabel("Percent" if metric.startswith("pct_") else "Count per cell")
    fig.tight_layout()
    fig.savefig(out / "{}_qc_distributions.png".format(tag), dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 5))
    points = ax.scatter(
        x.obs["total_counts"], x.obs["n_genes_by_counts"],
        c=x.obs["pct_counts_mt"], cmap="viridis", s=9, alpha=0.65, linewidths=0
    )
    fig.colorbar(points, ax=ax, label="Mitochondrial counts (%)")
    ax.set_xlabel("Total counts per cell")
    ax.set_ylabel("Detected genes per cell")
    ax.set_title("{}: counts versus detected genes".format(tag))
    fig.tight_layout()
    fig.savefig(out / "{}_counts_vs_genes.png".format(tag), dpi=180)
    plt.close(fig)


def run_scrublet(x: ad.AnnData, expected_rate: float) -> None:
    """Predict doublets while X still contains unnormalized raw counts."""
    if not 0 < expected_rate < 1:
        raise ValueError("expected_doublet_rate must be between 0 and 1.")
    if not sparse.issparse(x.X) and not np.issubdtype(np.asarray(x.X).dtype, np.integer):
        raise TypeError("Scrublet requires raw integer counts before normalization.")
    sc.pp.scrublet(x, expected_doublet_rate=float(expected_rate))
    needed = {"doublet_score", "predicted_doublet"}
    missing = needed.difference(x.obs.columns)
    if missing:
        raise RuntimeError("Scrublet did not produce: {}".format(sorted(missing)))


def apply_sample_filters(x: ad.AnnData, threshold: pd.Series, rows: list[dict],
                         out: Path) -> ad.AnnData:
    """Apply sample-specific cell cutoffs sequentially and record removals."""
    sample = str(x.obs["sample_id"].iloc[0])
    current, previous = x, x.n_obs
    steps = [
        ("minimum_counts", "total_counts", ">=", int(threshold.min_counts)),
        ("minimum_genes", "n_genes_by_counts", ">=", int(threshold.min_genes)),
        ("maximum_mitochondrial", "pct_counts_mt", "<=", float(threshold.max_mt_pct)),
        ("minimum_ribosomal", "pct_counts_ribo", ">=", float(threshold.min_ribo_pct)),
    ]
    rows.append({
        "sample_id": sample, "step": "starting_barcodes", "cells_remaining": previous,
        "cells_removed_at_step": 0, "genes_remaining": current.n_vars,
    })
    for name, metric, operator, cutoff in steps:
        values = current.obs[metric].to_numpy()
        keep = values >= cutoff if operator == ">=" else values <= cutoff
        current = current[keep].copy()
        remaining = current.n_obs
        rows.append({
            "sample_id": sample, "step": name, "cells_remaining": remaining,
            "cells_removed_at_step": previous - remaining if keep is not None else 0,
            "genes_remaining": current.n_vars,
        })
        previous = remaining

    run_scrublet(current, float(threshold.expected_doublet_rate))
    doublets = current.obs["predicted_doublet"].astype(bool).to_numpy()
    (out / "doublet_scores").mkdir(parents=True, exist_ok=True)
    current.obs[["doublet_score", "predicted_doublet"]].to_csv(
        out / "doublet_scores" / "{}_scores.csv".format(sample), index_label="barcode"
    )
    current = current[~doublets].copy()
    rows.append({
        "sample_id": sample, "step": "scrublet_doublet_removal",
        "cells_remaining": current.n_obs, "cells_removed_at_step": int(doublets.sum()),
        "genes_remaining": current.n_vars,
    })
    return current


def create_pseudobulk(counts: ad.AnnData, out: Path) -> None:
    """Export raw-count sums by sample; this is not a differential test."""
    x = counts.layers["counts"]
    samples = counts.obs["sample_id"].astype(str)
    rows = []
    for sample in samples.unique():
        mask = (samples == sample).to_numpy()
        rows.append(pd.Series(np.asarray(x[mask].sum(axis=0)).ravel(),
                              index=counts.var_names, name=sample))
    pd.DataFrame(rows).T.to_csv(out / "pseudobulk_raw_counts_by_sample.csv",
                                index_label="gene")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, default=Path("config/samples.csv"))
    parser.add_argument("--thresholds", type=Path, default=Path("config/thresholds.csv"))
    parser.add_argument("--out", type=Path, default=Path("results"))
    parser.add_argument("--n-pcs", type=int, required=True,
                        help="Choose after reviewing PCA variance-ratio plot.")
    parser.add_argument("--n-top-genes", type=int, default=2000)
    parser.add_argument("--n-neighbors", type=int, default=15)
    parser.add_argument("--leiden-resolution", type=float, default=0.5)
    parser.add_argument("--run-tsne", action="store_true")
    args = parser.parse_args()

    samples, thresholds = read_csv(args.samples), read_csv(args.thresholds)
    require_columns(samples, {"sample_id", "matrix_dir", "group", "donor_id"},
                    "samples table")
    require_columns(thresholds, {
        "sample_id", "min_counts", "min_genes", "max_mt_pct", "min_ribo_pct",
        "min_cells_per_gene", "expected_doublet_rate"
    }, "threshold table")
    if samples["sample_id"].duplicated().any() or thresholds["sample_id"].duplicated().any():
        raise ValueError("sample_id must be unique in both input tables.")
    by_sample = thresholds.set_index("sample_id")
    if set(samples.sample_id.astype(str)) != set(by_sample.index.astype(str)):
        raise ValueError("Samples and thresholds must contain identical sample IDs.")

    args.out.mkdir(parents=True, exist_ok=True)
    plot_dir = args.out / "figures"
    rows, filtered, before = [], [], []
    for _, row in samples.iterrows():
        x = load_matrix(row)
        annotate_genes(x)
        calculate_qc(x)
        save_qc_plots(x, plot_dir, "{}_before".format(row.sample_id))
        before.append(x.obs.assign(sample_id=str(row.sample_id)))
        threshold = by_sample.loc[str(row.sample_id)]
        x = apply_sample_filters(x, threshold, rows, args.out)
        calculate_qc(x)
        save_qc_plots(x, plot_dir, "{}_after_cell_filters".format(row.sample_id))
        filtered.append(x)

    # Concatenate raw counts only after sample-level filters. Do not correct embeddings here.
    combined = sc.concat(filtered, join="outer", label="concat_id", index_unique="-")
    combined.obs["sample_id"] = combined.obs["sample_id"].astype(str)
    annotate_genes(combined)
    calculate_qc(combined)

    min_cells = int(thresholds["min_cells_per_gene"].max())
    n_before = combined.n_vars
    sc.pp.filter_genes(combined, min_cells=min_cells)
    n_removed = n_before - combined.n_vars
    pd.DataFrame([{
        "minimum_cells_expressing_gene": min_cells, "genes_before": n_before,
        "genes_removed": n_removed, "genes_remaining": combined.n_vars
    }]).to_csv(args.out / "gene_filter_summary.csv", index=False)
    for sample in samples.sample_id.astype(str):
        rows.append({
            "sample_id": sample, "step": "minimum_cells_per_gene_global",
            "cells_remaining": int((combined.obs.sample_id == sample).sum()),
            "cells_removed_at_step": 0, "genes_remaining": combined.n_vars
        })

    pd.DataFrame(rows).to_csv(args.out / "sequential_filter_counts.csv", index=False)
    pd.concat(before).to_csv(args.out / "qc_metrics_before.csv", index_label="barcode")
    combined.obs.to_csv(args.out / "qc_metrics_after.csv", index_label="barcode")

    # Preserve counts. Normalization happens only after filtering and Scrublet.
    combined.layers["counts"] = combined.X.copy()
    create_pseudobulk(combined, args.out)
    combined.write_h5ad(args.out / "filtered_raw_counts.h5ad")
    sc.pp.normalize_total(combined, target_sum=1e4)
    sc.pp.log1p(combined)
    combined.raw = combined.copy()

    # Sample-aware ranking can reduce domination by a larger library; report this choice.
    sc.pp.highly_variable_genes(
        combined, flavor="seurat", n_top_genes=min(args.n_top_genes, combined.n_vars),
        batch_key="sample_id", subset=False
    )
    combined.var["highly_variable"] = combined.var["highly_variable"].fillna(False)
    hvg = combined[:, combined.var.highly_variable].copy()
    hvg.write_h5ad(args.out / "normalized_hvg.h5ad")
    sc.pp.scale(hvg, max_value=10)
    n_comps = min(50, hvg.n_obs - 1, hvg.n_vars - 1)
    if n_comps < 2 or args.n_pcs < 2 or args.n_pcs > n_comps:
        raise ValueError("n-pcs must be 2 through {} after QC.".format(n_comps))
    sc.tl.pca(hvg, n_comps=n_comps, svd_solver="arpack")
    sc.pl.pca_variance_ratio(hvg, n_pcs=n_comps, show=False)
    plt.savefig(plot_dir / "pca_variance_ratio.png", dpi=180, bbox_inches="tight")
    plt.close("all")

    sc.pp.neighbors(hvg, n_neighbors=args.n_neighbors, n_pcs=args.n_pcs)
    sc.tl.umap(hvg, min_dist=0.3, random_state=0)
    sc.tl.leiden(hvg, resolution=args.leiden_resolution, random_state=0)
    colors = [c for c in ("sample_id", "group", "donor_id", "leiden") if c in hvg.obs]
    sc.pl.umap(hvg, color=colors, show=False)
    plt.savefig(plot_dir / "umap_by_sample_group_cluster.png", dpi=180, bbox_inches="tight")
    plt.close("all")
    if args.run_tsne:
        sc.tl.tsne(hvg, n_pcs=args.n_pcs, random_state=0)
        sc.pl.tsne(hvg, color=colors, show=False)
        plt.savefig(plot_dir / "tsne_by_sample_group_cluster.png", dpi=180, bbox_inches="tight")
        plt.close("all")

    # Cluster markers are exploratory; these are not condition-level DE tests.
    sc.tl.rank_genes_groups(hvg, groupby="leiden", method="wilcoxon", use_raw=True)
    sc.get.rank_genes_groups_df(hvg, group=None).to_csv(
        args.out / "exploratory_cluster_markers.csv", index=False
    )
    sc.pl.rank_genes_groups_dotplot(hvg, n_genes=5, show=False)
    plt.savefig(plot_dir / "cluster_marker_dotplot.png", dpi=180, bbox_inches="tight")
    plt.close("all")
    hvg.write_h5ad(args.out / "scanpy_analysis.h5ad")


if __name__ == "__main__":
    main()
