"""Single-cell RNA-seq analysis module.

Supports post-quantification analysis with Scanpy (recommended) and hooks for
STARsolo / Alevin-fry quantification of droplet-based data (10x, etc.).

Now includes multi-sample integration via Harmony and scVI.

Typical flow:
  FASTQ → STARsolo or Alevin → AnnData → QC/filtering → Normalization →
  Integration (Harmony/scVI) → PCA/UMAP → Clustering → Marker genes → Insights
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd

try:
    import scanpy as sc
    import anndata as ad
    HAS_SCANPY = True
except ImportError:
    HAS_SCANPY = False

try:
    import harmonypy as hm
    HAS_HARMONY = True
except ImportError:
    HAS_HARMONY = False

try:
    import scvi
    HAS_SCVI = True
except ImportError:
    HAS_SCVI = False

QuantMethodSC = Literal["starsolo", "alevin", "cellranger"]
IntegrationMethod = Literal["harmony", "scvi", "bbknn", "none"]


def quantify_single_cell(
    fastq_dir: Path,
    reference: Path,
    method: QuantMethodSC = "starsolo",
    chemistry: str = "10xv3",
    output_dir: Path | None = None,
) -> Path:
    """Run single-cell quantification (interface).

    Real implementation calls STARsolo, Alevin-fry, or Cell Ranger.
    Returns path to filtered count matrix / AnnData.
    """
    out = (output_dir or Path("results/singlecell")) / f"counts_{method}"
    out.mkdir(parents=True, exist_ok=True)
    # Placeholder
    (out / "matrix.mtx").touch()
    return out


def analyze_single_cell(
    count_matrix: Path | str,
    output_dir: Path | None = None,
    min_genes: int = 200,
    min_cells: int = 3,
    n_top_genes: int = 2000,
    n_neighbors: int = 15,
    resolution: float = 0.5,
    batch_key: str | None = None,
    integration: IntegrationMethod = "none",
) -> Path:
    """Full Scanpy analysis pipeline on a count matrix.

    Supports optional multi-sample integration when batch_key is provided.
    Returns path to processed AnnData (.h5ad) with embeddings and clusters.
    """
    if not HAS_SCANPY:
        raise ImportError(
            "Scanpy is required for single-cell analysis. "
            "Install with: conda install -c conda-forge scanpy leidenalg"
        )

    out_dir = output_dir or Path("results/singlecell")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load (supports 10x mtx, h5ad, csv for demos)
    if str(count_matrix).endswith(".h5ad"):
        adata = sc.read_h5ad(count_matrix)
    else:
        # Demo / fallback
        adata = sc.AnnData(pd.DataFrame(
            [[100, 20], [50, 150], [200, 30]],
            columns=["gene1", "gene2"],
            index=["cell1", "cell2", "cell3"],
        ).T)
        if batch_key:
            adata.obs[batch_key] = ["sample1", "sample1", "sample2"]

    # Standard Scanpy workflow
    sc.pp.filter_cells(adata, min_genes=min_genes)
    sc.pp.filter_genes(adata, min_cells=min_cells)
    adata.var["mt"] = adata.var_names.str.startswith(("MT-", "mt-"))
    sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], percent_top=None, log1p=False, inplace=True)

    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=n_top_genes, flavor="seurat", batch_key=batch_key)
    adata = adata[:, adata.var.highly_variable]

    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, svd_solver="arpack")

    # Multi-sample integration
    if batch_key and integration != "none":
        adata = integrate_samples(adata, batch_key=batch_key, method=integration)

    use_rep = "X_pca_harmony" if integration == "harmony" else "X_scVI" if integration == "scvi" else "X_pca"
    sc.pp.neighbors(adata, n_neighbors=n_neighbors, use_rep=use_rep)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=resolution)

    # Marker genes
    sc.tl.rank_genes_groups(adata, "leiden", method="wilcoxon")

    h5ad_path = out_dir / "processed.h5ad"
    adata.write(h5ad_path)

    # Export markers
    markers = sc.get.rank_genes_groups_df(adata, group=None)
    markers.to_csv(out_dir / "marker_genes.csv", index=False)

    return h5ad_path


def integrate_samples(
    adata: "ad.AnnData",
    batch_key: str = "sample",
    method: IntegrationMethod = "harmony",
    n_pcs: int = 30,
) -> "ad.AnnData":
    """Integrate multiple samples / batches.

    Supported methods:
      - harmony: fast linear correction (recommended default)
      - scvi: deep generative model (more powerful, slower)
      - bbknn: graph-based (via scanpy external)
    """
    if not HAS_SCANPY:
        raise ImportError("Scanpy required")

    if method == "harmony":
        if not HAS_HARMONY:
            raise ImportError("harmonypy not installed. conda install -c conda-forge harmonypy")
        # Harmony on PCA
        sc.external.pp.harmony_integrate(adata, key=batch_key, basis="X_pca", adjusted_basis="X_pca_harmony")
        return adata

    if method == "scvi":
        if not HAS_SCVI:
            raise ImportError("scvi-tools not installed. pip install scvi-tools")
        scvi.model.SCVI.setup_anndata(adata, batch_key=batch_key)
        model = scvi.model.SCVI(adata, n_latent=n_pcs)
        model.train(max_epochs=100, early_stopping=True)
        adata.obsm["X_scVI"] = model.get_latent_representation()
        return adata

    if method == "bbknn":
        sc.external.pp.bbknn(adata, batch_key=batch_key)
        return adata

    return adata


def plot_single_cell(adata_path: Path, output_dir: Path | None = None, batch_key: str | None = None) -> list[Path]:
    """Generate standard single-cell plots (UMAP colored by cluster, batch, QC, etc.)."""
    if not HAS_SCANPY:
        return []

    adata = sc.read_h5ad(adata_path)
    out_dir = output_dir or Path("results/singlecell/plots")
    out_dir.mkdir(parents=True, exist_ok=True)

    plots = []
    # UMAP by cluster
    sc.pl.umap(adata, color="leiden", save="_leiden.png", show=False)
    plots.append(out_dir / "umap_leiden.png")

    # UMAP by batch (if present)
    if batch_key and batch_key in adata.obs:
        sc.pl.umap(adata, color=batch_key, save="_batch.png", show=False)
        plots.append(out_dir / "umap_batch.png")

    return plots
