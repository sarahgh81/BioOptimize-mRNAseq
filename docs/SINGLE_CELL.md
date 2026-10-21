# Single-cell RNA-seq Support

BioOptimize-mRNAseq now supports droplet-based single-cell RNA-seq (10x Genomics and compatible protocols) in addition to bulk mRNA-seq, including **multi-sample integration**.

## Recommended Tools

| Step | Tool | Notes |
|------|------|-------|
| Quantification | **STARsolo** | Fast, accurate, built into recent STAR |
| Alternative quant | Alevin-fry | Memory efficient |
| Analysis | **Scanpy** | PCA, UMAP, Leiden clustering, markers |
| Integration | **Harmony**, **scVI**, BBKNN | Multi-sample batch correction |

## Multi-sample Integration

When you have multiple samples or batches, use integration to remove technical variation while preserving biology.

| Method | Speed | Strength | When to use |
|--------|-------|----------|-------------|
| **Harmony** | Fast | Linear correction on PCA | Default choice for most studies |
| **scVI** | Slower | Deep generative model | Complex batches, large datasets |
| BBKNN | Fast | Graph-based | Quick neighbor correction |

### Example

```python
from pipeline.singlecell import analyze_single_cell

# adata must have a column in .obs identifying the sample/batch
processed = analyze_single_cell(
    count_matrix="results/combined.h5ad",
    batch_key="sample",
    integration="harmony",   # or "scvi"
    resolution=0.5,
)
```

Or call integration separately:

```python
from pipeline.singlecell import integrate_samples
import scanpy as sc

adata = sc.read_h5ad("qc_normalized.h5ad")
adata = integrate_samples(adata, batch_key="sample", method="harmony")
```

## Quick Workflow

1. **Quantify** (interface ready; implement real call):
   ```python
   from pipeline.singlecell import quantify_single_cell
   quantify_single_cell(fastq_dir="data/10x", reference="refs/hg38", method="starsolo")
   ```

2. **Analyze** (with optional integration):
   ```python
   from pipeline.singlecell import analyze_single_cell
   h5ad = analyze_single_cell(
       "results/singlecell/counts.h5ad",
       batch_key="sample",
       integration="harmony",
       resolution=0.5,
   )
   ```

3. **Get AI advice**:
   ```python
   from pipeline.advisor import AIParameterAdvisor
   advice = AIParameterAdvisor().suggest(assay="single_cell", expected_cells=10000)
   print(AIParameterAdvisor().pretty(advice))
   ```

## Configuration

See the `single_cell:` section in `config/default.yaml` for tunable parameters (min_genes, resolution, integration method, etc.).

## Environment

The conda environment includes:
- `scanpy`, `anndata`, `leidenalg`, `umap-learn`
- `harmonypy` (for Harmony)
- Optional: `scvi-tools` (install via pip for scVI)

```bash
conda env update -f environment.yml --prune
# Optional for scVI:
pip install scvi-tools
```

## Next Steps (Roadmap)

- Full STARsolo / Alevin subprocess wrappers
- Interactive Streamlit dashboard for UMAP exploration
- Cell type annotation hooks (CellTypist, scType)
- Differential abundance testing across samples
