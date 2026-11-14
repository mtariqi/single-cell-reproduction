# Single-cell RNA-seq quality control and exploratory analysis

## Abstract
[Complete after analysis. State the dataset, QC approach, retained cells and genes, main exploratory results, and limitations. Include only results computed from authorized data.]

## Background and study question
[Describe the approved biological question and design. Distinguish an in-vitro lipid accumulation phenotype from confirmed adipocyte differentiation.]

## Data and design
| Sample | Biological replicate or donor | Condition | Starting cells | Starting genes |
|---|---|---|---:|---:|
| [sample] | [verified metadata] | [verified metadata] | [n] | [n] |

Describe the 10x chemistry, the matrix type, and whether Cell Ranger web summary metrics were available. The original barcode-rank plot must come from unfiltered Cell Ranger output.

## Methods
Describe per-sample QC and the evidence for each threshold; sequential cell filtering; Scrublet input and expected rate; gene-prevalence filter; normalization; highly variable gene selection; PCA and PC choice; neighbor graph; UMAP or t-SNE settings; clustering resolution; merge or integration decision; software versions; and random seeds.

## Results

### Cell Ranger sequencing and barcode QC
[Insert source-derived barcode-rank and library metrics.]

### Per-cell QC before and after filtering
[Insert per-sample total-count, detected-gene, mitochondrial, and ribosomal distributions and counts-versus-genes plots.]

### Thresholds and filtering yield
| Sample | Step | Threshold | Cells before | Removed | Cells after | Genes after |
|---|---|---|---:|---:|---:|---:|
| [sample] | [step] | [value and rationale] | [n] | [n] | [n] | [n] |

### Doublet assessment
[Report Scrublet configuration, predicted count and rate, and expected rate. Predictions are not confirmed biological doublets.]

### Normalization, HVGs, PCA, embedding, and clusters
[Report plots, selected parameters, the evidence used to choose PCs and clustering resolution, and sensitivity checks. Color embeddings by sample, donor, and condition.]

### Exploratory markers and biological interpretation
[Summarize cluster markers and planned pathway analysis. Treat exploratory findings as hypotheses for validation.]

## Discussion
Explain threshold tradeoffs, sample-quality differences, whether shared or sample-specific cutoffs were justified, whether integration was warranted, and limitations. Cell numbers do not substitute for independent biological replicates.

## Group reflection
- What was clear:
- What was challenging:
- How the group resolved issues:
- What the group learned:
- Contributions:

## Reproducibility and data governance
Record code, software versions, parameters, output locations, and authorized data provenance. Do not deposit restricted data or unpublished findings publicly without permission.

## References
Wolf, F. A., Angerer, P., & Theis, F. J. (2018). SCANPY: Large-scale single-cell gene expression data analysis. *Genome Biology, 19*, Article 15. https://doi.org/10.1186/s13059-017-1382-0

Wolock, S. L., Lopez, R., & Klein, A. M. (2019). Scrublet: Computational identification of cell doublets in single-cell transcriptomic data. *Cell Systems, 8*(4), 281–291.e9. https://doi.org/10.1016/j.cels.2018.11.005

Luecken, M. D., & Theis, F. J. (2019). Current best practices in single-cell RNA-seq analysis: A tutorial. *Molecular Systems Biology, 15*(6), e8746. https://doi.org/10.15252/msb.20188746

Korsunsky, I., Millard, N., Fan, J., Slowikowski, K., Zhang, F., Wei, K., ... Raychaudhuri, S. (2019). Fast, sensitive and accurate integration of single-cell data with Harmony. *Nature Methods, 16*, 1289–1296. https://doi.org/10.1038/s41592-019-0619-0

Squair, J. W., Gautier, M., Kathe, C., et al. (2021). Confronting false discoveries in single-cell differential expression. *Nature Communications, 12*, Article 5692. https://doi.org/10.1038/s41467-021-25960-2
