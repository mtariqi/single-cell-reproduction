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

To reproduce this analysis, create a new conda environment and activate it:

```bash
conda env create -f environment.yml
conda activate single-cell-reproduction
jupyter lab


Ensure you list these key commands:
## 🚀 How to Reproduce
### Prerequisites
Install dependencies using conda:
```bash
conda env create -f environment.yml
conda activate single-cell-tutorial

Run the Tutorial

jupyter notebook
Then open one of the notebooks under latest_notebook/ and run all cells.
📊 Expected Output

Processed AnnData (.h5ad) file

UMAP and t-SNE plots of cell clusters

Marker gene expression visualizations

Reproducible figures from the original study

📄 Reference

Luecken, M. D., & Theis, F. J. (2019). Current best practices in single-cell RNA-seq analysis: a tutorial.
Molecular Systems Biology, 15(6), e8746.
https://doi.org/10.15252/msb.20188746

✨ Author (Reproduction)

Md Tariqul Islam (Tariq)
📍 Toronto, Canada
🔗 github.com/mtariqi
