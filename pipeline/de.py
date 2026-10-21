"""Differential expression analysis (DESeq2 / edgeR wrappers)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def run_differential_expression(
    count_matrix: Path | pd.DataFrame,
    design: Path | pd.DataFrame,
    method: str = "deseq2",
    output_dir: Path | None = None,
) -> Path:
    """Run DE analysis and return results table."""
    out_dir = output_dir or Path("results/de")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Placeholder for rpy2 or subprocess R call
    results = out_dir / f"de_results_{method}.csv"
    demo = pd.DataFrame({
        "gene_id": ["ENSG000001", "ENSG000002"],
        "log2FoldChange": [1.8, -0.4],
        "padj": [0.001, 0.45],
        "baseMean": [1460, 365],
    })
    demo.to_csv(results, index=False)
    return results
