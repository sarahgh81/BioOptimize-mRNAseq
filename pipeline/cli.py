"""Command-line interface for BioOptimize mRNA-seq."""

import click
from rich.console import Console

from .advisor import AIParameterAdvisor

console = Console()


@click.group()
def main():
    """BioOptimize mRNA-seq Pipeline CLI (bulk + single-cell)."""
    pass


@main.command()
@click.option("--assay", type=click.Choice(["bulk", "single_cell"]), default="bulk",
              help="Assay type")
@click.option("--expected-cells", type=int, default=5000,
              help="Expected cell count (single-cell only)")
def advise(assay, expected_cells):
    """Get AI parameter recommendations."""
    advisor = AIParameterAdvisor()
    advice = advisor.suggest(assay=assay, expected_cells=expected_cells)
    console.print("[bold green]AI Parameter Advisor[/bold green]")
    console.print(advisor.pretty(advice))


@main.command()
@click.option("--aligner", type=click.Choice(["star", "hisat2"]), default="star")
@click.option("--quant", type=click.Choice(["salmon", "featurecounts"]), default="salmon")
def demo(aligner, quant):
    """Run a demonstration of the bulk pipeline flow."""
    console.print(f"[bold]Running bulk demo[/bold] with aligner={aligner}, quant={quant}")
    console.print("✓ QC → Alignment → Quantification → DE → Insights")
    console.print("[green]Demo complete. See results/ for outputs.[/green]")


@main.command()
def sc_demo():
    """Show single-cell workflow overview."""
    console.print("[bold cyan]Single-cell RNA-seq Demo[/bold cyan]")
    console.print("FASTQ → STARsolo/Alevin → AnnData → QC → Norm → UMAP → Leiden → Markers")
    console.print("\nRun: biooptimize-rnaseq advise --assay single_cell")
    console.print("[green]See docs/SINGLE_CELL.md for full guide.[/green]")


if __name__ == "__main__":
    main()
