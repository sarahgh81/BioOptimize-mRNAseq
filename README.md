# BioOptimize mRNA-seq Pipeline 🧬🤖

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/sarahgh81/BioOptimize-mRNAseq/actions/workflows/ci.yml/badge.svg)](https://github.com/sarahgh81/BioOptimize-mRNAseq/actions)
[![Stars](https://img.shields.io/github/stars/sarahgh81/BioOptimize-mRNAseq)](https://github.com/sarahgh81/BioOptimize-mRNAseq/stargazers)

**AI-assisted, reproducible RNA-seq analysis — bulk and single-cell — from raw FASTQ to biological insights.**

Part of the BioOptimize AI ecosystem — an intelligent workspace for molecular biology that turns samples into insights.

## Why BioOptimize-mRNAseq?

Traditional RNA-seq pipelines are powerful but opaque. This project makes them:

- **Transparent** — clear comparisons between STAR vs HISAT2, Salmon vs featureCounts, and STARsolo vs Alevin
- **AI-augmented** — intelligent parameter suggestions for both bulk and single-cell experiments
- **Reproducible** — Conda/Snakemake-ready, version-controlled configs
- **Educational & Professional** — beautiful docs, examples, and CI
- **Dual-mode** — one toolkit for bulk mRNA-seq **and** single-cell RNA-seq

## Features

| Stage | Bulk | Single-cell | Highlights |
|-------|------|-------------|------------|
| QC | FastQC, MultiQC | mito %, gene counts | Automated reports |
| Alignment / Quant | **STAR**, **HISAT2**, Salmon | **STARsolo**, Alevin-fry | Side-by-side comparison |
| Analysis | DESeq2, edgeR | Scanpy (PCA, UMAP, Leiden) | Marker genes, clusters |
| Visualization | PCA, volcano, heatmaps | UMAP, QC violins, markers | Interactive options |
| AI Layer | Parameter advisor | sc-specific recommendations | Extensible for LLMs |

## Quick Start

```bash
# Clone
git clone https://github.com/sarahgh81/BioOptimize-mRNAseq.git
cd BioOptimize-mRNAseq

# Install (recommended: conda)
conda env create -f environment.yml
conda activate biooptimize-rnaseq

# Or pip
pip install -e .

# Bulk demo
python -m pipeline.demo

# Single-cell advice
python -c "
from pipeline.advisor import AIParameterAdvisor
print(AIParameterAdvisor().pretty(
    AIParameterAdvisor().suggest(assay='single_cell', expected_cells=8000)
))
"
```

## Pipeline Overview

**Bulk**
```
FASTQ → QC → Alignment (STAR/HISAT2) → Quantification → DE → Insights
```

**Single-cell**
```
FASTQ → STARsolo/Alevin → AnnData → QC → Norm → PCA/UMAP → Leiden → Markers
```

### Single-cell example

```python
from pipeline.singlecell import analyze_single_cell

# After quantification (or with a demo matrix)
processed = analyze_single_cell(
    count_matrix="results/singlecell/counts.h5ad",
    min_genes=200,
    resolution=0.5,
)
print(f"Processed AnnData saved to {processed}")
```

## Project Structure

```
BioOptimize-mRNAseq/
├── pipeline/
│   ├── align.py          # Bulk alignment
│   ├── singlecell.py     # Scanpy analysis + sc quant interface
│   ├── advisor.py        # AI recommendations (bulk + sc)
│   └── ...
├── config/default.yaml  # Includes single_cell section
├── examples/
├── docs/
├── tests/
├── environment.yml      # Now includes scanpy, leidenalg, etc.
└── README.md
```

## Installation Details

See [docs/INSTALL.md](docs/INSTALL.md) for full setup including reference genomes and tool dependencies.

For single-cell you will also want:
- STARsolo (included with STAR ≥ 2.7.9a)
- or Alevin-fry
- Scanpy ecosystem (installed via the conda environment)

## Citation

If you use this in research or teaching:

```bibtex
@software{BioOptimize_mRNAseq,
  author = {Ghasemi, Sarah},
  title = {BioOptimize mRNA-seq: AI-Assisted RNA-seq Pipeline (Bulk + Single-cell)},
  year = {2026},
  url = {https://github.com/sarahgh81/BioOptimize-mRNAseq}
}
```

## Related Projects

- [PCR_AI](https://github.com/sarahgh81/PCR_AI) — Governance core for mRNA research agents
- BioOptimize AI — Full Sample-to-Insight molecular biology workspace

## Contributing

PRs welcome! Please open an issue first for major changes. All contributions must respect research-use-only guidelines.

---

**Built with ❤️ for researchers who want clarity, not black boxes.**

> For Research Use Only. Not for diagnostic or clinical decision-making.
