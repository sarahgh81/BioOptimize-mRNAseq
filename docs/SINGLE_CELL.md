# Single-cell RNA-seq Support

BioOptimize-mRNAseq now supports droplet-based single-cell RNA-seq (10x Genomics and compatible protocols) in addition to bulk mRNA-seq.

## Recommended Tools

| Step | Tool | Notes |
|------|------|-------|
| Quantification | **STARsolo** | Fast, accurate, built into recent STAR |
| Alternative quant | Alevin-fry | Memory efficient |
| Analysis | **Scanpy** | PCA, UMAP, Leiden clustering, markers |
| Integration | Harmony / scVI | Multi-sample (planned) |

## Quick Workflow

1. **Quantify** (interface ready; implement real call):
   ```python
   from pipeline.singlecell import quantify_single_cell
   quantify_single_cell(fastq_dir="data/10x", reference="refs/hg38", method="starsolo")
   ```

2. **Analyze** with Scanpy:
   ```python
   from pipeline.singlecell import analyze_single_cell
   h5ad = analyze_single_cell("results/singlecell/counts.h5ad", resolution=0.5)
   ```

3. **Get AI advice**:
   ```python
   from pipeline.advisor import AIParameterAdvisor
   advice = AIParameterAdvisor().suggest(assay="single_cell", expected_cells=10000)
   print(AIParameterAdvisor().pretty(advice))
   ```

## Configuration

See the `single_cell:` section in `config/default.yaml` for tunable parameters (min_genes, resolution, etc.).

## Environment

The conda environment now includes:
- `scanpy`
- `anndata`
- `leidenalg`
- `umap-learn`

Re-create or update your environment after pulling the latest changes.

## Next Steps (Roadmap)

- Full STARsolo / Alevin subprocess wrappers
- Multi-sample integration (Harmony, scVI)
- Interactive Streamlit dashboard for UMAP exploration
- Cell type annotation hooks (CellTypist, scType)
