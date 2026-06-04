import json
from pathlib import Path
from ..models.observability_report import ObservabilityReport

class ObservabilityReportReader:
    def read(self, path: Path) -> ObservabilityReport:
        if not path.exists():
            raise FileNotFoundError(f"Observability report not found at: {path}")
        
        try:
            with open(path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in observability report: {e}") from e
        
        return ObservabilityReport.model_validate(data)
