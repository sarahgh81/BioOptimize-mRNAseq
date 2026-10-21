"""AI Parameter Advisor — suggests optimal settings based on experiment design.

Supports both bulk RNA-seq and single-cell RNA-seq.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Advice:
    assay: str  # "bulk" or "single_cell"
    aligner: str
    reason: str
    threads: int
    quant_method: str
    de_method: str
    notes: list[str]
    # Single-cell specific
    resolution: float | None = None
    n_neighbors: int | None = None


class AIParameterAdvisor:
    """Lightweight rule-based + extensible advisor.

    In full BioOptimize AI this can call an LLM with experiment metadata.
    """

    def suggest(
        self,
        organism: str = "human",
        read_length: int = 150,
        paired: bool = True,
        goal: str = "differential_expression",
        sample_count: int = 6,
        assay: str = "bulk",  # "bulk" or "single_cell"
        expected_cells: int | None = None,
    ) -> Advice:
        if assay == "single_cell":
            return self._suggest_single_cell(
                organism=organism,
                expected_cells=expected_cells or 5000,
                goal=goal,
            )

        # Bulk path (original)
        aligner = "star" if sample_count >= 4 else "hisat2"
        reason = (
            "STAR preferred for higher unique mapping and splice-aware accuracy "
            "on standard mammalian RNA-seq"
            if aligner == "star"
            else "HISAT2 is faster and sufficient for smaller cohorts"
        )

        notes = [
            "Use --twopassMode Basic for STAR when detecting novel junctions.",
            "Salmon is recommended for transcript-level quantification (faster, accurate).",
            "DESeq2 is the default for most designs; edgeR for more complex models.",
        ]

        return Advice(
            assay="bulk",
            aligner=aligner,
            reason=reason,
            threads=8 if sample_count > 8 else 4,
            quant_method="salmon",
            de_method="deseq2",
            notes=notes,
        )

    def _suggest_single_cell(
        self,
        organism: str,
        expected_cells: int,
        goal: str,
    ) -> Advice:
        quant = "starsolo" if expected_cells > 2000 else "alevin"
        reason = (
            "STARsolo is fast, accurate, and well-supported for 10x-style data"
            if quant == "starsolo"
            else "Alevin-fry is memory-efficient for smaller or mixed datasets"
        )

        resolution = 0.4 if expected_cells < 3000 else 0.6
        notes = [
            "Filter cells with <200 genes and genes expressed in <3 cells.",
            "Use mitochondrial percentage <20% as a starting QC cutoff.",
            "Leiden clustering with resolution 0.4–0.8 works well for most tissues.",
            "Rank genes by Wilcoxon for marker identification.",
            "Consider Harmony or scVI for multi-sample integration.",
        ]

        return Advice(
            assay="single_cell",
            aligner="starsolo",
            reason=reason,
            threads=16,
            quant_method=quant,
            de_method="wilcoxon",
            notes=notes,
            resolution=resolution,
            n_neighbors=15,
        )

    def pretty(self, advice: Advice) -> str:
        lines = [
            f"Assay: {advice.assay.replace('_', ' ').title()}",
            f"Recommended method: {advice.aligner.upper()} / {advice.quant_method} — {advice.reason}",
            f"Threads: {advice.threads}",
            f"DE / markers: {advice.de_method}",
        ]
        if advice.resolution is not None:
            lines.append(f"Leiden resolution: {advice.resolution}")
            lines.append(f"Neighbors: {advice.n_neighbors}")
        lines.append("Tips:")
        lines.extend(f"  • {n}" for n in advice.notes)
        return "\n".join(lines)
