# 🧫 Single-Cell RNA-seq Reproduction Study (Theis Lab Tutorial)

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Updated](https://img.shields.io/github/last-commit/mtariqi/single-cell-reproduction?color=yellow)

# 1. Clear Overview
This repository reproduces the single-cell RNA-seq tutorial from Luecken & Theis (2019),
“Current best practices in single-cell RNA-seq analysis: a tutorial” (Mol. Syst. Biol.).
The goal is to learn reproducible single-cell workflows, visualization, and clustering.

📄 **Original paper:** [https://doi.org/10.15252/msb.20188746](https://doi.org/10.15252/msb.20188746)  
💻 **Original source code:** [https://github.com/theislab/single-cell-tutorial](https://github.com/theislab/single-cell-tutorial)

---

## 2. 📘 Project Overview
This tutorial demonstrates an end-to-end single-cell RNA-seq analysis pipeline including:

1. **Preprocessing** — QC, normalization, feature selection  
2. **Integration** — batch correction and data harmonization  
3. **Dimensionality reduction** — PCA, t-SNE, UMAP  
4. **Clustering** — Leiden/Louvain clustering  
5. **Cell type annotation and marker identification**  
6. **Visualization** — heatmaps, trajectory plots, and cluster UMAPs  

## Project Summary:
This repository reproduces the single-cell RNA-seq tutorial by Luecken & Theis (2019), demonstrating best practices in preprocessing, clustering, visualization, and interpretation of single-cell transcriptomic data. The workflow uses Python and Scanpy within Jupyter notebooks to explore the Haber et al. (2018) mouse gut dataset, replicating key analyses from the original publication. Designed as a graduate-level reproducibility exercise, this project emphasizes transparency, reproducibility, and open science in computational biology, serving as a foundation for extending single-cell workflows to new datasets or integrating advanced tools such as Seurat, Harmony, and scVI.
---
⚙️ 3. Reproduction Steps
conda env create -f environment.yml
conda activate single-cell-tutorial
jupyter notebook
```
latest_notebook/
 ├── 01_preprocessing.ipynb
 ├── 02_clustering.ipynb
 ├── 03_visualization.ipynb
```

## 📓 Notebook Summary

| Notebook | Description |
|-----------|--------------|
| [Case-study_Mouse-intestinal-epithelium_1906.ipynb](notebooks/Case-study_Mouse-intestinal-epithelium_1906.ipynb) | Reproduction of the Haber et al. (2018) mouse intestinal single-cell RNA-seq dataset. Includes preprocessing, dimensionality reduction, clustering, and cell-type annotation using the Scanpy pipeline. |
| [gprofiler_plotting.py](scripts/gprofiler_plotting.py) | Utility script for enrichment analysis and visualization of marker genes. |

---

## 🧠 Results Preview

This section will be updated with representative outputs from the analysis:
- **UMAP plots** showing major intestinal cell types  
- **Marker gene heatmaps**  
- **Pathway enrichment** using g:Profiler  
- **Cluster identity annotations**  

*(Plots will be added after reproducing the analysis locally.)*

---

## 💻 Environment and Reproducibility

- Python ≥ 3.9  
- Scanpy, AnnData, and gprofiler-official  
- Compatible with Jupyter Notebook, Snakemake, or Nextflow  
- MIT License (open for reuse in research and teaching)


## ⚙️ Environment Setup

To reproduce this single-cell RNA-seq analysis locally, you can use the provided Conda environment.

### 1️⃣ Create and Activate the Environment

```bash
conda env create -f environment.yml
conda activate single-cell-reproduction

Run the Tutorial

jupyter notebook
Then open one of the notebooks under latest_notebook/ and run all cells.
📊 Expected Output

Processed AnnData (.h5ad) file

UMAP and t-SNE plots of cell clusters

Marker gene expression visualizations

Reproducible figures from the original study

## 🧪 Environment Validation

After activating the environment, you can run the following simple test to confirm that all dependencies were installed correctly and that the environment is ready for analysis.

### ✅ Test the installation

Launch Python in your terminal and try importing the core packages:

```bash
python

Then run:
import scanpy as sc
import anndata
import pandas as pd
import matplotlib.pyplot as plt

print("Scanpy version:", sc.__version__)
print("AnnData version:", anndata.__version__)
print("Pandas version:", pd.__version__)

🧬 Optional: Run a quick Scanpy test

You can also load a built-in dataset to verify that plotting works:

import scanpy as sc

adata = sc.datasets.pbmc3k()   # small 3k PBMC test dataset
sc.pp.pca(adata)
sc.pl.pca(adata, color='CST3')

## 🧠 Results Preview

This section showcases representative outputs from the reproduced single-cell RNA-seq analysis of the **Haber et al. (2018)** mouse intestinal dataset.

### 🧩 1️⃣ UMAP Projection
Visualization of cell clusters after dimensionality reduction and Leiden clustering.

<p align="center">
  <img src="results/umap_clusters.png" alt="UMAP Clustering" width="600"/>
</p>

---

### 🧬 2️⃣ Marker Gene Expression
Heatmap displaying marker genes across major intestinal cell types.

<p align="center">
  <img src="results/marker_heatmap.png" alt="Marker Gene Heatmap" width="600"/>
</p>

---

### 🔍 3️⃣ Pathway Enrichment
Pathway analysis performed with **g:Profiler** highlighting enriched biological pathways per cluster.

<p align="center">
  <img src="results/pathway_enrichment.png" alt="Pathway Enrichment" width="600"/>
</p>

---

### 🧾 Notes
- All results are generated from the provided Jupyter notebook:  
  [`Case-study_Mouse-intestinal-epithelium_1906.ipynb`](notebooks/Case-study_Mouse-intestinal-epithelium_1906.ipynb)
- Figures can be regenerated by re-running the notebook after setting up the environment.
- Once images are produced, save them under a `results/` directory and push to GitHub.

---

## 📚 Citation & References

If you use or adapt this repository for academic or research purposes, please cite the original tutorial and dataset authors as follows:

### 🔬 Primary References

**Luecken, M. D., & Theis, F. J. (2019).**  
_Current best practices in single-cell RNA-seq analysis: a tutorial._  
*Nature Methods, 16*(1), 45–54.  
https://doi.org/10.1038/s41592-018-0250-3

**Haber, A. L., Biton, M., Rogel, N., Herbst, R. H., Shekhar, K., Smillie, C., Burgin, G., Delorey, T. M., Howitt, M. R., Katz, Y., Tirosh, I., Beyaz, S., Dionne, D., Zhang, M., Raychowdhury, R., Garrett, W. S., Rozenblatt-Rosen, O., Shi, H. N., Yilmaz, Ö. H., ... Regev, A. (2017).**  
_A single-cell survey of the small intestinal epithelium._  
*Nature, 551*(7680), 333–339.  
https://doi.org/10.1038/nature24489

---

### 🧩 Tutorial Repository Reference

**Theis Lab. (2019).**  
_single-cell-tutorial: Reproducible single-cell RNA-seq analysis pipeline using Scanpy._  
GitHub repository: [https://github.com/theislab/single-cell-tutorial](https://github.com/theislab/single-cell-tutorial)

---

### 🧠 Citation for This Reproduction

If referencing my reproduction work directly:

**Islam, M. T. (2025).**  
_Reproduction of “Current best practices in single-cell RNA-seq analysis” using Python and Scanpy._  
GitHub repository: [https://github.com/mtariqi/single-cell-reproduction](https://github.com/mtariqi/single-cell-reproduction)


✨ Author (Reproduction)

Md Tariqul Islam (Tariq)
📍 Toronto, Canada
🔗 github.com/mtariqi
