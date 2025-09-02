"""Console script for arctic_monthly_dynamics."""

import typer
from rich.console import Console

from arctic_monthly_dynamics import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for arctic_monthly_dynamics."""
    console.print("Replace this message by putting your code into "
               "arctic_monthly_dynamics.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
