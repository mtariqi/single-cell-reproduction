# 🧫 Single-Cell RNA-seq Reproduction Study (Theis Lab Tutorial)

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Updated](https://img.shields.io/github/last-commit/mtariqi/single-cell-reproduction?color=yellow)


This repository reproduces the case study from **Luecken & Theis (2019)**,  
*"Current best practices in single-cell RNA-seq analysis: a tutorial."*  
_Molecular Systems Biology, 15(6):e8746._

📄 **Original paper:** [https://doi.org/10.15252/msb.20188746](https://doi.org/10.15252/msb.20188746)  
💻 **Original source code:** [https://github.com/theislab/single-cell-tutorial](https://github.com/theislab/single-cell-tutorial)

---

## 📘 Project Overview
This tutorial demonstrates an end-to-end single-cell RNA-seq analysis pipeline including:

1. **Preprocessing** — QC, normalization, feature selection  
2. **Integration** — batch correction and data harmonization  
3. **Dimensionality reduction** — PCA, t-SNE, UMAP  
4. **Clustering** — Leiden/Louvain clustering  
5. **Cell type annotation and marker identification**  
6. **Visualization** — heatmaps, trajectory plots, and cluster UMAPs  

---

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
