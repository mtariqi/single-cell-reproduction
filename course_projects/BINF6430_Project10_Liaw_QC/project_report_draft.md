# Single-Cell RNA Sequencing Quality Control

## Project 10 | Liaw VSMC pilot samples

> **WORKING DRAFT — not submission-ready.** Replace bracketed prompts with results from the Liaw sample analyses, insert exported plots, and complete the group reflection. PBMC tutorial values are not Liaw results.


| Report details | Entry |

| --- | --- |

| Course | BINF 6430 |

| Student | Md Tariqul Islam |

| Group members | [Add group member names] |

| Date | [Enter submission date] |

| Analysis platform | Northeastern Explorer; JupyterLab; Scanpy |

Before submission: Replace each bracketed prompt with results from the Liaw sample analyses, insert the exported plots, and complete the group reflection. The PBMC tutorial values are not reported as Liaw results.

# Executive Summary

This report describes quality control and filtering of four 10x Flex single-cell RNA-seq matrices from the Liaw VSMC pilot. We will use per-sample distributions of total counts, detected genes, mitochondrial fraction, and ribosomal fraction to choose and justify thresholds. Scrublet will identify predicted doublets from raw counts before normalization. [Complete after analysis: summarize the final thresholds, cells and genes retained, and the main differences observed among samples.]

# 1. Study Context and Objective

The goal is to remove low-quality cell barcodes and uninformative genes while retaining viable VSMCs and biologically meaningful variation. The class data are described as a Liaw Lab VSMC pilot with four samples collected under standard SMC media (DM) or adipogenic media (AdipoB). This report focuses on quality control rather than downstream differential expression.

# 2. Data and Sample Design

The Cell Ranger filtered feature-barcode matrices are read from the course data directory. Each sample is analyzed separately at the QC stage so that differences in library depth and quality can be assessed before deciding whether a shared or sample-specific threshold is appropriate.

| Sample folder | Donor label | Culture condition | Initial cells | Initial genes |

| --- | --- | --- | --- | --- |

| 49-AdipoB | 49 | AdipoB | [n] | [n] |

| 49-DM | 49 | DM | [n] | [n] |

| 916-AdipoB | 916 | AdipoB | [n] | [n] |

| 916-DM | 916 | DM | [n] | [n] |

Matrix location pattern: `/courses/BINF6430.202710/data/LiawData/10x_FRP_12-16-22/analysis/MMC-1/outs/per_sample_outs/<SAMPLE>/count/sample_filtered_feature_bc_matrix/`

The assignment describes the pilot as healthy versus AAA VSMCs. Confirm and report the donor-to-disease-status mapping from the course metadata before labeling the samples by disease group.

# 3. Analysis Workflow

For each sample, the filtered 10x matrix is loaded into an AnnData object with Scanpy. Gene names are made unique, and QC annotations are created for mitochondrial and ribosomal genes. Hemoglobin fraction is omitted from the final filtering criteria because the assignment notes that hemoglobin genes are not expected in these cultured VSMCs. The PBMC demo notebook is used only to learn the workflow; its cutoffs are not carried over.

- Inspect total counts and detected genes per cell, plus mitochondrial and ribosomal percentages.

- Choose cutoffs from each sample’s distributions and scatterplots; document whether thresholds are shared or sample-specific.

- Apply the cell filters sequentially and record the cells remaining after each step.

- Filter genes expressed in fewer than the selected number of cells.

- Run Scrublet on raw counts, record predicted doublets, and remove flagged barcodes.

- Normalize retained counts and log-transform for downstream exploratory analyses; save the filtered AnnData object.

# 4. QC Thresholds and Rationale

Use the observed Liaw sample plots to complete the threshold table. Explain the evidence for each cutoff and note any sample-specific departures.

| Metric | Chosen threshold | Shared or per sample? | Rationale / plot evidence |

| --- | --- | --- | --- |

| Minimum total counts per cell | [value(s)] | [shared / per sample] | [Describe low-count tail and selected boundary] |

| Minimum detected genes per cell | [value(s)] | [shared / per sample] | [Describe low-gene tail and selected boundary] |

| Maximum mitochondrial counts (%) | [value(s)] | [shared / per sample] | [Describe upper tail and selected boundary] |

| Minimum ribosomal counts (%) | [value(s)] | [shared / per sample] | [Describe lower tail and selected boundary] |

| Minimum cells expressing each gene | [value] | [shared] | [Describe prevalence plot and rationale] |

| Doublet detection | Scrublet; record settings | [per sample] | [Report flagged rate and expected rate] |

Thresholds are operational QC decisions, not universal biological constants. Mitochondrial percentage can rise in stressed or damaged cells, while ribosomal percentage may reflect both technical quality and cell state. We therefore interpret these metrics jointly with total counts and detected genes and inspect retained and removed cells after filtering.

# 5. QC Plots Before and After Filtering

Insert readable plots for all four samples. Include axis labels, units, sample names, and threshold lines. If plots are faceted, identify each panel clearly.

[Insert exported QC plot here]

Figure 1. Pre-filter distributions of total counts, detected genes, mitochondrial percentage, and ribosomal percentage for all four samples.

[Insert exported QC plot here]

Figure 2. Pre-filter total counts versus detected genes, colored by mitochondrial percentage, with selected thresholds shown.

[Insert exported QC plot here]

Figure 3. Post-filter QC distributions for all four samples using the same metrics and scales as Figure 1 where practical.

[Insert exported QC plot here]

Figure 4. Post-filter counts-versus-genes plots with threshold lines and mitochondrial percentage for all four samples.

# 6. Filtering Results

Record the number of cells remaining and removed at each sequential step. Use the sample name on each row. The “removed” count is the difference from the previous step.

| Sample | Filtering step | Cells remaining | Cells removed at step | Genes remaining |

| --- | --- | --- | --- | --- |

| 49-AdipoB | Starting barcodes | [n] | [n] | [n] |

| 49-AdipoB | Minimum counts | [n] | [n] | [n] |

| 49-AdipoB | Mitochondrial filter | [n] | [n] | [n] |

| 49-AdipoB | Ribosomal filter | [n] | [n] | [n] |

| 49-AdipoB | Minimum genes | [n] | [n] | [n] |

| 49-AdipoB | Doublet removal | [n] | [n] | [n] |

| 49-AdipoB | Final retained | [n] | [n] | [n] |

| 49-DM | Starting barcodes | [n] | [n] | [n] |

| 49-DM | Minimum counts | [n] | [n] | [n] |

| 49-DM | Mitochondrial filter | [n] | [n] | [n] |

| 49-DM | Ribosomal filter | [n] | [n] | [n] |

| 49-DM | Minimum genes | [n] | [n] | [n] |

| 49-DM | Doublet removal | [n] | [n] | [n] |

| 49-DM | Final retained | [n] | [n] | [n] |

| 916-AdipoB | Starting barcodes | [n] | [n] | [n] |

| 916-AdipoB | Minimum counts | [n] | [n] | [n] |

| 916-AdipoB | Mitochondrial filter | [n] | [n] | [n] |

| 916-AdipoB | Ribosomal filter | [n] | [n] | [n] |

| 916-AdipoB | Minimum genes | [n] | [n] | [n] |

| 916-AdipoB | Doublet removal | [n] | [n] | [n] |

| 916-AdipoB | Final retained | [n] | [n] | [n] |

| 916-DM | Starting barcodes | [n] | [n] | [n] |

| 916-DM | Minimum counts | [n] | [n] | [n] |

| 916-DM | Mitochondrial filter | [n] | [n] | [n] |

| 916-DM | Ribosomal filter | [n] | [n] | [n] |

| 916-DM | Minimum genes | [n] | [n] | [n] |

| 916-DM | Doublet removal | [n] | [n] | [n] |

| 916-DM | Final retained | [n] | [n] | [n] |

## 6.1 Doublet Summary

| Sample | Cells entering Scrublet | Predicted doublets | Detected rate | Expected rate | Cells retained |

| --- | --- | --- | --- | --- | --- |

| 49-AdipoB | [n] | [n] | [%] | [%] | [n] |

| 49-DM | [n] | [n] | [%] | [%] | [n] |

| 916-AdipoB | [n] | [n] | [%] | [%] | [n] |

| 916-DM | [n] | [n] | [%] | [%] | [n] |

# 7. Interpretation and Limitations

[Summarize how the four samples differed in library depth, detected genes, mitochondrial and ribosomal fractions, and retained cell numbers. Explain whether one threshold set was appropriate across samples or whether per-sample cutoffs were better supported by the plots.]

The pilot includes four sample libraries and is intended for QC practice. Any interpretation should account for the limited number of biological samples and avoid treating individual cells as independent biological replicates. Threshold choices may affect cell yield and gene representation; the group should report the criteria and counts transparently so the filtering can be evaluated and reproduced.

# 8. Group Reflection

Complete this section as a group. Describe the actual analysis process and discussion rather than leaving the prompts in the submitted PDF.

What was clear: [Describe which QC concepts or steps were straightforward and why.]

What was challenging: [Describe difficulties choosing thresholds, interpreting distributions, or running the workflow.]

How the group resolved issues: [Record the code checks, plots, documentation, or discussion that helped.]

What the group learned: [Explain how threshold choices changed the retained cell/gene set and what you would improve next time.]

Contribution summary: [Briefly state how the group divided analysis, interpretation, and report preparation.]

# 9. Reproducibility Notes

| Item | Record |

| --- | --- |

| Notebook | scanpy_qc_filtering_Student.ipynb (adapted for Liaw matrices) |

| Scanpy / Python versions | [record from active BINF6430 kernel] |

| Input matrix source | Course LiawData per-sample filtered feature-barcode matrices |

| Output files | [list .h5ad files, plots, and summary table paths] |

| Filtering order | Counts → mitochondrial → ribosomal → genes per cell → genes per sample prevalence → Scrublet |

| Normalization | After cell and doublet filtering; target sum and log transform recorded in notebook |

# References

Wolf, F. A., Angerer, P., & Theis, F. J. (2018). SCANPY: Large-scale single-cell gene expression data analysis. Genome Biology, 19, Article 15. https://doi.org/10.1186/s13059-017-1382-0

Wolock, S. L., Lopez, R., & Klein, A. M. (2019). Scrublet: Computational identification of cell doublets in single-cell transcriptomic data. Cell Systems, 8(4), 281–291.e9. https://doi.org/10.1016/j.cels.2018.11.005
