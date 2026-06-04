import json
import pytest
from pathlib import Path
from odl_dashboards.readers.observability_report_reader import ObservabilityReportReader
from odl_dashboards.models.observability_report import ObservabilityReport

def test_read_valid_report(tmp_path):
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
    
    reader = ObservabilityReportReader()
    report = reader.read(report_file)
    
    assert isinstance(report, ObservabilityReport)
    assert report.metrics.run_id == "test-run"
    assert report.health_status == "healthy"

def test_read_missing_file():
    reader = ObservabilityReportReader()
    with pytest.raises(FileNotFoundError, match="Observability report not found"):
        reader.read(Path("non_existent.json"))

def test_read_invalid_json(tmp_path):
    report_file = tmp_path / "invalid.json"
    report_file.write_text("{invalid json")
    
    reader = ObservabilityReportReader()
    with pytest.raises(ValueError, match="Invalid JSON"):
        reader.read(report_file)
