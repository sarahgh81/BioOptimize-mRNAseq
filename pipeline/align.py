"""Alignment module supporting STAR and HISAT2 with side-by-side comparison."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import pandas as pd

Aligner = Literal["star", "hisat2"]


@dataclass
class AlignmentResult:
    sample: str
    aligner: Aligner
    mapping_rate: float
    uniquely_mapped: int
    multi_mapped: int
    runtime_seconds: float
    output_bam: Path

    def summary_row(self) -> dict:
        return {
            "sample": self.sample,
            "aligner": self.aligner,
            "mapping_rate_%": round(self.mapping_rate * 100, 2),
            "uniquely_mapped": self.uniquely_mapped,
            "multi_mapped": self.multi_mapped,
            "runtime_min": round(self.runtime_seconds / 60, 1),
        }


def run_alignment(
    fastq_r1: Path,
    fastq_r2: Path | None,
    reference: Path,
    aligner: Aligner = "star",
    threads: int = 8,
    output_dir: Path | None = None,
) -> AlignmentResult:
    """Run a single alignment.

    In production this calls the actual STAR or HISAT2 binary.
    This implementation provides the interface and mock metrics for demos.
    """
    # Placeholder for real subprocess calls
    # e.g., subprocess.run(["STAR", "--runThreadN", str(threads), ...])
    mapping_rate = 0.92 if aligner == "star" else 0.89
    unique = 12_500_000 if aligner == "star" else 11_800_000
    multi = 800_000 if aligner == "star" else 1_100_000
    runtime = 420 if aligner == "star" else 310

    out = (output_dir or Path("results/alignment")) / f"{fastq_r1.stem}_{aligner}.bam"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.touch()

    return AlignmentResult(
        sample=fastq_r1.stem,
        aligner=aligner,
        mapping_rate=mapping_rate,
        uniquely_mapped=unique,
        multi_mapped=multi,
        runtime_seconds=runtime,
        output_bam=out,
    )


def compare_aligners(
    samples: str | Path | pd.DataFrame,
    reference: str | Path,
    aligners: list[Aligner] | None = None,
    threads: int = 8,
) -> pd.DataFrame:
    """Compare STAR vs HISAT2 across samples. Returns summary DataFrame."""
    if aligners is None:
        aligners = ["star", "hisat2"]

    if isinstance(samples, (str, Path)):
        df = pd.read_csv(samples)
    else:
        df = samples

    results = []
    for _, row in df.iterrows():
        for aln in aligners:
            res = run_alignment(
                fastq_r1=Path(row["fastq_r1"]),
                fastq_r2=Path(row["fastq_r2"]) if "fastq_r2" in row and pd.notna(row["fastq_r2"]) else None,
                reference=Path(reference),
                aligner=aln,
                threads=threads,
            )
            results.append(res.summary_row())

    summary = pd.DataFrame(results)
    return summary
