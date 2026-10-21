# BioOptimize mRNA-seq Pipeline 🧬🤖

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/sarahgh81/BioOptimize-mRNAseq/actions/workflows/ci.yml/badge.svg)](https://github.com/sarahgh81/BioOptimize-mRNAseq/actions)
[![Stars](https://img.shields.io/github/stars/sarahgh81/BioOptimize-mRNAseq)](https://github.com/sarahgh81/BioOptimize-mRNAseq/stargazers)

**AI-assisted, reproducible mRNA-seq analysis from raw FASTQ to differential expression insights.**

Part of the BioOptimize AI ecosystem — an intelligent workspace for molecular biology that turns samples into insights.

## Why BioOptimize-mRNAseq?

Traditional RNA-seq pipelines are powerful but opaque. This project makes them:

- **Transparent** — clear comparisons between STAR vs HISAT2, Salmon vs featureCounts
- **AI-augmented** — intelligent parameter suggestions and result interpretation hooks
- **Reproducible** — Conda/Snakemake-ready, version-controlled configs
- **Educational & Professional** — beautiful docs, examples, and CI

## Features

| Stage | Tools Supported | Highlights |
|-------|-----------------|------------|
| QC | FastQC, MultiQC | Automated reports |
| Alignment | **STAR**, **HISAT2** | Side-by-side comparison mode |
| Quantification | Salmon (quasi), featureCounts, RSEM | Transcript & gene level |
| Differential Expression | DESeq2, edgeR | R integration via rpy2 or standalone |
| Visualization | PCA, volcano, heatmaps | Interactive Plotly options |
| AI Layer | Parameter advisor, result summarizer | Extensible for LLMs |

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

# Run example
python -m pipeline.demo --aligner star --quant salmon
```

## Pipeline Overview

```
FASTQ → QC → Alignment (STAR/HISAT2) → Quantification → DE Analysis → Insights
                 ↘─────────────────────↗
                   AI Parameter Advisor
```

### Example: Compare Aligners

```python
from pipeline.align import compare_aligners

results = compare_aligners(
    samples="examples/samples.csv",
    reference="hg38",
    aligners=["star", "hisat2"]
)
print(results.summary())  # Mapping rates, unique reads, runtime
```

## Project Structure

```
BioOptimize-mRNAseq/
├── pipeline/           # Core analysis modules
├── config/             # YAML configs
├── examples/           # Sample sheets & demo data pointers
├── docs/               # Detailed guides
├── tests/              # Unit & integration tests
├── .github/workflows/  # CI
├── environment.yml
└── README.md
```

## Installation Details

See [docs/INSTALL.md](docs/INSTALL.md) for full setup including reference genomes and tool dependencies (STAR, HISAT2, Salmon, R packages).

## Citation

If you use this in research or teaching:

```bibtex
@software{BioOptimize_mRNAseq,
  author = {Ghasemi, Sarah},
  title = {BioOptimize mRNA-seq: AI-Assisted RNA-seq Pipeline},
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
