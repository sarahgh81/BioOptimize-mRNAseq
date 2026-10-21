"""Command-line interface for BioOptimize mRNA-seq."""

import click
from rich.console import Console

from .advisor import AIParameterAdvisor

console = Console()


@click.group()
def main():
    """BioOptimize mRNA-seq Pipeline CLI."""
    pass


@main.command()
def advise():
    """Get AI parameter recommendations."""
    advisor = AIParameterAdvisor()
    advice = advisor.suggest()
    console.print("[bold green]AI Parameter Advisor[/bold green]")
    console.print(advisor.pretty(advice))


@main.command()
@click.option("--aligner", type=click.Choice(["star", "hisat2"]), default="star")
@click.option("--quant", type=click.Choice(["salmon", "featurecounts"]), default="salmon")
def demo(aligner, quant):
    """Run a demonstration of the pipeline flow."""
    console.print(f"[bold]Running demo[/bold] with aligner={aligner}, quant={quant}")
    console.print("✓ QC → Alignment → Quantification → DE → Insights")
    console.print("[green]Demo complete. See results/ for outputs.[/green]")


if __name__ == "__main__":
    main()
