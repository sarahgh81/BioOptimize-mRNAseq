"""Runnable demonstration of the full pipeline flow."""

from rich.console import Console

from .advisor import AIParameterAdvisor
from .align import compare_aligners

console = Console()


def main():
    console.rule("[bold cyan]BioOptimize mRNA-seq Demo[/bold cyan]")

    advisor = AIParameterAdvisor()
    advice = advisor.suggest(organism="human", sample_count=6, goal="differential_expression")
    console.print(advisor.pretty(advice))
    console.print()

    console.print("[bold]Aligner comparison (demo metrics):[/bold]")
    # In a real run this would use examples/samples.csv
    console.print("STAR  → 92.1% mapped, 12.5M unique")
    console.print("HISAT2 → 89.4% mapped, 11.8M unique")
    console.print()

    console.print("[green]✓ Pipeline skeleton ready. Implement real tool calls for production.[/green]")
    console.rule()


if __name__ == "__main__":
    main()
