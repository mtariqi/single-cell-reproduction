# BINF6430 Project 10 — Liaw VSMC single-cell QC

Working Scanpy project documentation for quality control of the four Liaw VSMC pilot sample matrices described in the BINF6430 assignment.

## Status

**Draft only.** The report template has explicit placeholders for sample-derived thresholds, QC plots, filtering counts, Scrublet output, and the group reflection. Do not treat the PBMC tutorial results or cutoffs as Liaw results. Complete the analysis from the course-provided matrices before citing final results.

## Contents

- [`project_report_draft.md`](project_report_draft.md) — report draft aligned with the submission checklist.

## Scope and data handling

The assignment describes four 10x Flex filtered feature-barcode matrices: 49-AdipoB, 49-DM, 916-AdipoB, and 916-DM. The course data are not included in this repository. No raw matrices, cell-level data, or `.h5ad` outputs are committed. Use your authorized Explorer course-data paths and record software versions and output locations in your final report.

## Required completion items

1. Before- and after-filtering QC plots for all samples.
2. Thresholds and evidence-based rationale, derived from Liaw distributions.
3. Sequential cell and gene counts, including Scrublet-predicted doublets.
4. A short comparison and limitations discussion.
5. A truthful group reflection and contribution summary.
