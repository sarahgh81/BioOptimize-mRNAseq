# Installation Guide

## Prerequisites

- Conda or Mamba
- ~50 GB free disk for reference genomes (optional for full runs)
- R ≥ 4.2 (installed via the environment)

## Recommended: Conda

```bash
conda env create -f environment.yml
conda activate biooptimize-rnaseq
pip install -e .
```

## Reference Genomes

Download and index (example for human):

```bash
# STAR index (one-time)
STAR --runMode genomeGenerate \
  --genomeDir refs/hg38_star \
  --genomeFastaFiles hg38.fa \
  --sjdbGTFfile genes.gtf \
  --sjdbOverhang 149

# Salmon index
salmon index -t transcripts.fa -i refs/hg38_salmon
```

Update paths in `config/default.yaml`.

## Verify

```bash
biooptimize-rnaseq advise
python -m pytest tests/
```
