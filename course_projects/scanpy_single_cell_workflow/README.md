# Reproducible Scanpy single-cell RNA-seq workflow

A data-free scaffold for quality control and exploratory analysis of 10x feature-barcode matrices. It records per-sample QC, sequential filtering, Scrublet scores, normalization, highly variable genes, PCA, UMAP, clustering, and exploratory cluster markers.

## Data and sharing

This repository contains no experimental matrices, cell-level data, sample identifiers, or unpublished findings. Use this workflow only with data you are authorized to access. Do not publish restricted study data or results without permission from the data owner and course or institution.

## Workflow

1. Create config/samples.csv from config/samples_template.csv using the authorized metadata and matrix directories.
2. Inspect Cell Ranger web_summary.html or equivalent metrics when available. A filtered feature-barcode matrix does not contain the empty-droplet barcodes needed to reproduce the original barcode-rank plot.
3. Generate initial per-sample QC plots. Choose thresholds from observed distributions and complete a copy of config/thresholds_template.csv. Do not reuse cutoffs from another tissue or tutorial.
4. Apply the cell filters sequentially and run Scrublet on raw counts. Set expected doublet rate from the loading design, not an unverified default.
5. Review the PCA variance-ratio plot, select PCs, and rerun. Record parameters and sensitivity checks.
6. Interpret UMAP and Leiden clusters as exploratory. Cluster markers are not inferential condition-level differential expression.
7. For condition comparisons, use sample-level pseudobulk only when there are enough independent biological replicates. Cells are not biological replicates.

## Run

~~~bash
conda env create -f environment.yml
conda activate scanpy-qc
cp config/samples_template.csv config/samples.csv
cp config/thresholds_template.csv config/thresholds.csv
# Edit both CSV files using authorized metadata and QC evidence.
python scripts/scanpy_workflow.py --n-pcs 20
~~~

The example PC count is a placeholder. Choose the number after inspecting results/figures/pca_variance_ratio.png. For an optional t-SNE view, add --run-tsne.

## Outputs

- results/figures/: pre/post QC distributions, counts-versus-genes plots, PCA variance ratio, UMAP, optional t-SNE, and marker dotplot.
- results/sequential_filter_counts.csv: cells removed at each step.
- results/gene_filter_summary.csv: gene-prevalence filtering summary.
- results/doublet_scores/: per-cell Scrublet scores.
- results/pseudobulk_raw_counts_by_sample.csv: raw-count sums per sample for later sample-level modeling.
- results/*.h5ad: intermediate analysis objects; ignored by Git.

## Interpretation safeguards

- Mitochondrial and ribosomal fractions support QC; they are not universal pass/fail rules.
- Report the Cell Ranger barcode-rank plot separately from filtered-cell QC plots.
- Compare simple concatenation with integration only if sample or batch structure suggests it is needed. Integration changes embeddings, not original counts. Check cell numbers and marker expression before and after correction.
- Record normalization, HVG, PC, neighbor, UMAP, clustering, and doublet parameters.
- Avoid condition-level inference from cell-level p-values when independent biological replicates are insufficient.
