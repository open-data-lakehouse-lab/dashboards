from pydantic import BaseModel
from .observability_report import ObservabilityReport

class Dashboard(BaseModel):
    title: str
    report: ObservabilityReport
