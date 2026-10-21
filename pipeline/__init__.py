"""BioOptimize mRNA-seq Pipeline

AI-assisted, reproducible analysis from FASTQ to differential expression.
Now with single-cell RNA-seq support.
"""

__version__ = "0.2.0"

from .align import compare_aligners, run_alignment
from .quantify import quantify_samples
from .de import run_differential_expression
from .advisor import AIParameterAdvisor
from .singlecell import analyze_single_cell, quantify_single_cell, plot_single_cell

__all__ = [
    "compare_aligners",
    "run_alignment",
    "quantify_samples",
    "run_differential_expression",
    "AIParameterAdvisor",
    "analyze_single_cell",
    "quantify_single_cell",
    "plot_single_cell",
]
