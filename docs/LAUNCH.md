# BioOptimize-mRNAseq Launch Announcement

**AI-assisted, transparent RNA-seq pipeline — bulk + single-cell + multi-sample integration.**

## One-liner
Open-source pipeline that makes mRNA-seq analysis clear and reproducible: STAR vs HISAT2 comparison, Salmon quantification, DESeq2, Scanpy, and Harmony/scVI multi-sample integration, plus an AI parameter advisor.

## Why it exists
Most RNA-seq workflows are powerful but opaque. BioOptimize-mRNAseq focuses on transparency, education, and practical AI assistance so researchers can understand *why* a tool or parameter was chosen.

## Key Features
- Bulk: STAR / HISAT2 comparison, Salmon, DESeq2 / edgeR
- Single-cell: STARsolo / Alevin interface + full Scanpy workflow
- Multi-sample integration: Harmony (default), scVI, BBKNN
- AI Parameter Advisor for both bulk and single-cell
- Conda + Snakemake ready, MIT licensed

## Quick Start
```bash
git clone https://github.com/sarahgh81/BioOptimize-mRNAseq.git
cd BioOptimize-mRNAseq
conda env create -f environment.yml
conda activate biooptimize-rnaseq
pip install -e .
biooptimize-rnaseq advise --assay single_cell
```

## Links
- Repository: https://github.com/sarahgh81/BioOptimize-mRNAseq
- Single-cell guide: docs/SINGLE_CELL.md
- Part of the BioOptimize AI ecosystem

## Suggested Social Posts

### Reddit (r/bioinformatics or r/singlecell)
Title: Open-source bulk + scRNA-seq pipeline with transparent tool comparisons and Harmony integration

Body:
I built BioOptimize-mRNAseq — an open-source, educational RNA-seq pipeline that supports both bulk and single-cell analysis.

Highlights:
- Side-by-side STAR vs HISAT2 comparison
- Scanpy workflow with optional Harmony / scVI multi-sample integration
- AI parameter advisor that suggests settings based on your experiment
- Conda environment + Snakemake skeleton
- MIT licensed

Repo: https://github.com/sarahgh81/BioOptimize-mRNAseq

Feedback and contributions welcome. Research use only.

### Show HN
Title: Show HN: BioOptimize-mRNAseq – transparent AI-assisted RNA-seq pipeline (bulk + single-cell)

Body:
I wanted an RNA-seq pipeline that is both practical and transparent. BioOptimize-mRNAseq lets you compare aligners, run bulk DE or single-cell analysis (Scanpy + Harmony), and get AI-suggested parameters.

It is early but fully open source and structured for learning and extension.

https://github.com/sarahgh81/BioOptimize-mRNAseq

### X / LinkedIn
Just released BioOptimize-mRNAseq — an open-source pipeline for transparent bulk + single-cell RNA-seq analysis.

✓ STAR vs HISAT2 comparison  
✓ Scanpy + Harmony multi-sample integration  
✓ AI parameter advisor  
✓ Conda + Snakemake ready

https://github.com/sarahgh81/BioOptimize-mRNAseq

Built for researchers who want clarity, not black boxes. Feedback welcome!
