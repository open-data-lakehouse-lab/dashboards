from odl_dashboards.renderers.static_html import StaticHTMLRenderer
from odl_dashboards.models.dashboard import Dashboard
from odl_dashboards.models.observability_report import ObservabilityReport, Metrics, FailedStep

def test_render_expected_fields():
    metrics = Metrics(
        run_id="run-123",
        workflow_name="workflow-abc",
        dataset_id="dataset-xyz",
        resource="resource-1",
        status="success",
        total_steps=5,
        successful_steps=5,
        failed_steps=0,
        artifact_count=2,
        duration_seconds=50.0
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="healthy",
        health_message="Everything is fine",
        failed_steps=[]
    )
    dashboard = Dashboard(title="Test Dashboard", report=report)
    
    renderer = StaticHTMLRenderer()
    html = renderer.render(dashboard)
    
    assert "<!DOCTYPE html>" in html
    assert "<title>Test Dashboard</title>" in html
    assert "Open Data Lakehouse Lab" in html
    assert "run-123" in html
    assert "workflow-abc" in html
    assert "dataset-xyz" in html
    assert "healthy" in html
    assert "Everything is fine" in html
    assert "50.00s" in html

def test_render_failed_steps():
    metrics = Metrics(
        run_id="run-123",
        workflow_name="workflow-abc",
        dataset_id="dataset-xyz",
        resource="resource-1",
        status="failed",
        total_steps=5,
        successful_steps=4,
        failed_steps=1,
        artifact_count=2,
        duration_seconds=50.0
    )
    failed_step = FailedStep(
        step_name="step-fail",
        return_code=1,
        stderr="Something went wrong <script>alert('hack')</script>"
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="unhealthy",
        health_message="Found errors",
        failed_steps=[failed_step]
    )
    dashboard = Dashboard(title="Test Dashboard", report=report)
    
    renderer = StaticHTMLRenderer()
    html = renderer.render(dashboard)
    
    assert "step-fail" in html
    assert "Something went wrong &lt;script&gt;alert(&#x27;hack&#x27;)&lt;/script&gt;" in html
    assert "<h2>Failed Steps</h2>" in html

def test_html_escaping():
    metrics = Metrics(
        run_id="run-123",
        workflow_name="<b>dangerous</b>",
        dataset_id="dataset-xyz",
        resource="resource-1",
        status="success",
        total_steps=5,
        successful_steps=5,
        failed_steps=0,
        artifact_count=2,
        duration_seconds=50.0
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="healthy",
        health_message="All good",
        failed_steps=[]
    )
    dashboard = Dashboard(title="<script>alert(1)</script>", report=report)
    
    renderer = StaticHTMLRenderer()
    html = renderer.render(dashboard)
    
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "&lt;b&gt;dangerous&lt;/b&gt;" in html

def test_render_none_duration():
    metrics = Metrics(
        run_id="run-123",
        workflow_name="workflow-abc",
        dataset_id="dataset-xyz",
        resource="resource-1",
        status="success",
        total_steps=5,
        successful_steps=5,
        failed_steps=0,
        artifact_count=2,
        duration_seconds=None
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="healthy",
        health_message="Everything is fine",
        failed_steps=[]
    )
    dashboard = Dashboard(title="Test Dashboard", report=report)
    
    renderer = StaticHTMLRenderer()
    html = renderer.render(dashboard)
    
    assert "N/A" in html
