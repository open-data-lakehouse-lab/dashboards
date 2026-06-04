from typing import List
from pydantic import BaseModel

class FailedStep(BaseModel):
    step_name: str
    return_code: int
    stderr: str

class Metrics(BaseModel):
    run_id: str
    workflow_name: str
    dataset_id: str
    resource: str
    status: str
    total_steps: int
    successful_steps: int
    failed_steps: int
    artifact_count: int
    duration_seconds: float | None = None

class ObservabilityReport(BaseModel):
    metrics: Metrics
    health_status: str
    health_message: str
    failed_steps: List[FailedStep]
