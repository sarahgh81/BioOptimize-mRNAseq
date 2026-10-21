"""BioOptimize mRNA-seq Pipeline

AI-assisted, reproducible analysis from FASTQ to differential expression.
"""

__version__ = "0.1.0"

from .align import compare_aligners, run_alignment
from .quantify import quantify_samples
from .de import run_differential_expression
from .advisor import AIParameterAdvisor

__all__ = [
    "compare_aligners",
    "run_alignment",
    "quantify_samples",
    "run_differential_expression",
    "AIParameterAdvisor",
]
