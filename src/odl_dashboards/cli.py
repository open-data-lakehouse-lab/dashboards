from pathlib import Path

import typer
from pydantic import ValidationError

from .readers.observability_report_reader import ObservabilityReportReader
from .renderers.static_html import StaticHTMLRenderer
from .writers.dashboard_writer import DashboardWriter
from .models.dashboard import Dashboard

app = typer.Typer(help="Open Data Lakehouse Lab Dashboards CLI")
render_app = typer.Typer(help="Render commands")
app.add_typer(render_app, name="render")

@app.command()
def version() -> None:
    """Print the version of odl-dashboards."""
    typer.echo("0.1.0")

@render_app.command(name="observability")
def render_observability(
    report_path: Path = typer.Option(..., "--report-path", "-r", help="Path to the report JSON file"),
    output_dir: Path = typer.Option(Path("./dashboard"), "--output-dir", "-o", help="Directory to save the dashboard"),
) -> None:
    """Render an observability dashboard from a report."""
    try:
        reader = ObservabilityReportReader()
        report = reader.read(report_path)
        
        dashboard = Dashboard(
            title=f"Observability Report: {report.metrics.workflow_name}",
            report=report
        )
        
        renderer = StaticHTMLRenderer()
        html_content = renderer.render(dashboard)
        
        writer = DashboardWriter()
        generated_path = writer.write(html_content, output_dir)
        
        typer.echo(f"Dashboard generated successfully: {generated_path}")
    except (FileNotFoundError, ValueError, ValidationError) as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
