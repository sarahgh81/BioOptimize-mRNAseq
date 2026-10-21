"""AI Parameter Advisor — suggests optimal settings based on experiment design."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Advice:
    aligner: str
    reason: str
    threads: int
    quant_method: str
    de_method: str
    notes: list[str]


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
    ) -> Advice:
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
            aligner=aligner,
            reason=reason,
            threads=8 if sample_count > 8 else 4,
            quant_method="salmon",
            de_method="deseq2",
            notes=notes,
        )

    def pretty(self, advice: Advice) -> str:
        lines = [
            f"Recommended aligner: {advice.aligner.upper()} — {advice.reason}",
            f"Threads: {advice.threads}",
            f"Quantification: {advice.quant_method}",
            f"DE method: {advice.de_method}",
            "Tips:",
            *[f"  • {n}" for n in advice.notes],
        ]
        return "\n".join(lines)
