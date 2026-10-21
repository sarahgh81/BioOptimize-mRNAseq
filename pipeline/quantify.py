"""Quantification: Salmon (preferred), featureCounts, RSEM."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd

QuantMethod = Literal["salmon", "featurecounts", "rsem"]


def quantify_samples(
    alignment_or_fastq: Path,
    annotation: Path,
    method: QuantMethod = "salmon",
    output_dir: Path | None = None,
) -> Path:
    """Run quantification and return path to count matrix."""
    out_dir = output_dir or Path("results/quantification")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Placeholder — real implementation calls salmon quant or featureCounts
    matrix = out_dir / f"counts_{method}.csv"
    # Demo matrix
    demo = pd.DataFrame({
        "gene_id": ["ENSG000001", "ENSG000002", "ENSG000003"],
        "sample1": [1500, 320, 890],
        "sample2": [1420, 410, 910],
    })
    demo.to_csv(matrix, index=False)
    return matrix
