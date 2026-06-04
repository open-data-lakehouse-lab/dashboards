import json
from typer.testing import CliRunner
from odl_dashboards.cli import app

runner = CliRunner(mix_stderr=False)

def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.stdout

def test_render_observability_success(tmp_path):
    report_data = {
        "metrics": {
            "run_id": "test-run",
            "workflow_name": "test-workflow",
            "dataset_id": "test-dataset",
            "resource": "test-resource",
            "status": "success",
            "total_steps": 10,
            "successful_steps": 10,
            "failed_steps": 0,
            "artifact_count": 5,
            "duration_seconds": 100.5
        },
        "health_status": "healthy",
        "health_message": "All good",
        "failed_steps": []
    }
    report_file = tmp_path / "report.json"
    report_file.write_text(json.dumps(report_data))
    output_dir = tmp_path / "dashboard"
    
    result = runner.invoke(app, [
        "render", "observability",
        "--report-path", str(report_file),
        "--output-dir", str(output_dir)
    ])
    
    assert result.exit_code == 0
    assert "Dashboard generated successfully" in result.stdout
    assert (output_dir / "index.html").exists()

def test_render_observability_missing_file():
    result = runner.invoke(app, [
        "render", "observability",
        "--report-path", "non_existent.json"
    ])
    assert result.exit_code == 1
    assert "Error:" in result.stderr

def test_render_unsupported_type():
    result = runner.invoke(app, [
        "render", "unsupported",
        "--report-path", "any.json"
    ])
    assert result.exit_code != 0
    assert "No such command" in result.stdout or "No such command" in result.stderr
