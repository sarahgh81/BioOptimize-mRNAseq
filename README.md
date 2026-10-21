# BioOptimize mRNA-seq Pipeline 🧬🤖

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/sarahgh81/BioOptimize-mRNAseq/actions/workflows/ci.yml/badge.svg)](https://github.com/sarahgh81/BioOptimize-mRNAseq/actions)
[![Stars](https://img.shields.io/github/stars/sarahgh81/BioOptimize-mRNAseq)](https://github.com/sarahgh81/BioOptimize-mRNAseq/stargazers)

**AI-assisted, reproducible RNA-seq analysis — bulk and single-cell (with multi-sample integration) — from raw FASTQ to biological insights.**

Part of the BioOptimize AI ecosystem — an intelligent workspace for molecular biology that turns samples into insights.

> **Latest (v0.3):** Multi-sample integration (Harmony / scVI / BBKNN) is now supported.  
> See [CHANGELOG.md](CHANGELOG.md) and [docs/LAUNCH.md](docs/LAUNCH.md).

## Why BioOptimize-mRNAseq?

Traditional RNA-seq pipelines are powerful but opaque. This project makes them:

- **Transparent** — clear comparisons between STAR vs HISAT2, Salmon vs featureCounts, and STARsolo vs Alevin
- **AI-augmented** — intelligent parameter suggestions for both bulk and single-cell experiments
- **Reproducible** — Conda/Snakemake-ready, version-controlled configs
- **Educational & Professional** — beautiful docs, examples, and CI
- **Dual-mode** — one toolkit for bulk mRNA-seq **and** single-cell RNA-seq
- **Multi-sample ready** — Harmony, scVI, and BBKNN integration for multi-sample studies

## Features

| Stage | Bulk | Single-cell | Highlights |
|-------|------|-------------|------------|
| QC | FastQC, MultiQC | mito %, gene counts | Automated reports |
| Alignment / Quant | **STAR**, **HISAT2**, Salmon | **STARsolo**, Alevin-fry | Side-by-side comparison |
| Integration | — | **Harmony**, scVI, BBKNN | Multi-sample batch correction |
| Analysis | DESeq2, edgeR | Scanpy (PCA, UMAP, Leiden) | Marker genes, clusters |
| Visualization | PCA, volcano, heatmaps | UMAP by cluster & batch | Interactive options |
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

**Single-cell (with integration)**
```
FASTQ → STARsolo/Alevin → AnnData → QC → Norm → Integration → PCA/UMAP → Leiden → Markers
```

### Single-cell + multi-sample example

```python
from pipeline.singlecell import analyze_single_cell

processed = analyze_single_cell(
    count_matrix="results/combined.h5ad",
    batch_key="sample",
    integration="harmony",   # or "scvi"
    resolution=0.5,
)
print(f"Integrated AnnData saved to {processed}")
```

## Project Structure

```
BioOptimize-mRNAseq/
├── pipeline/
│   ├── align.py          # Bulk alignment
│   ├── singlecell.py     # Scanpy + integration (Harmony/scVI)
│   ├── advisor.py        # AI recommendations (bulk + sc)
│   └── ...
├── config/default.yaml  # Includes single_cell + integration section
├── examples/
├── docs/               # Includes SINGLE_CELL.md and LAUNCH.md
├── tests/
├── environment.yml      # scanpy, harmonypy, etc.
└── README.md
```

## Installation Details

See [docs/INSTALL.md](docs/INSTALL.md) and [docs/SINGLE_CELL.md](docs/SINGLE_CELL.md) for full setup.

For single-cell + integration:
- STARsolo (included with STAR ≥ 2.7.9a)
- Scanpy ecosystem + harmonypy (via conda environment)
- Optional: `pip install scvi-tools` for scVI

## Citation

If you use this in research or teaching:

```bibtex
@software{BioOptimize_mRNAseq,
  author = {Ghasemi, Sarah},
  title = {BioOptimize mRNA-seq: AI-Assisted RNA-seq Pipeline (Bulk + Single-cell + Integration)},
  year = {2026},
  url = {https://github.com/sarahgh81/BioOptimize-mRNAseq}
}
```

## Related Projects

- [PCR_AI](https://github.com/sarahgh81/PCR_AI) — Governance core for mRNA research agents
- BioOptimize AI — Full Sample-to-Insight molecular biology workspace

## Contributing

PRs welcome! Please open an issue first for major changes. All contributions must respect research-use-only guidelines.

See also: [docs/LAUNCH.md](docs/LAUNCH.md) for ready-to-use announcement posts.

---

**Built with ❤️ for researchers who want clarity, not black boxes.**

> For Research Use Only. Not for diagnostic or clinical decision-making.
