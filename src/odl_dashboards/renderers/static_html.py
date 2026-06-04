from ..models.dashboard import Dashboard
from ..utils.html import escape

class StaticHTMLRenderer:
    def render(self, dashboard: Dashboard) -> str:
        report = dashboard.report
        metrics = report.metrics
        
        failed_steps_html = ""
        if report.failed_steps:
            failed_steps_html = "<h2>Failed Steps</h2><table><tr><th>Step Name</th><th>Return Code</th><th>Error</th></tr>"
            for step in report.failed_steps:
                failed_steps_html += f"""
                <tr>
                    <td>{escape(step.step_name)}</td>
                    <td>{step.return_code}</td>
                    <td><pre>{escape(step.stderr)}</pre></td>
                </tr>
                """
            failed_steps_html += "</table>"

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(dashboard.title)}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f7f6;
        }}
        h1, h2 {{
            color: #2c3e50;
        }}
        .header {{
            border-bottom: 2px solid #3498db;
            margin-bottom: 20px;
            padding-bottom: 10px;
        }}
        .project-name {{
            font-size: 0.9em;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .card-title {{
            font-size: 0.8em;
            color: #7f8c8d;
            margin-bottom: 5px;
            text-transform: uppercase;
        }}
        .card-value {{
            font-size: 1.2em;
            font-weight: bold;
            color: #2c3e50;
        }}
        .status-success {{ color: #27ae60; }}
        .status-failed {{ color: #e74c3c; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        th, td {{
            text-align: left;
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        pre {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
            white-space: pre-wrap;
            word-break: break-all;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="project-name">Open Data Lakehouse Lab</div>
        <h1>{escape(dashboard.title)}</h1>
    </div>

    <div class="summary">
        <div class="card">
            <div class="card-title">Run ID</div>
            <div class="card-value">{escape(metrics.run_id)}</div>
        </div>
        <div class="card">
            <div class="card-title">Workflow</div>
            <div class="card-value">{escape(metrics.workflow_name)}</div>
        </div>
        <div class="card">
            <div class="card-title">Dataset</div>
            <div class="card-value">{escape(metrics.dataset_id)}</div>
        </div>
        <div class="card">
            <div class="card-title">Resource</div>
            <div class="card-value">{escape(metrics.resource)}</div>
        </div>
        <div class="card">
            <div class="card-title">Workflow Status</div>
            <div class="card-value {"status-success" if metrics.status.lower() == "success" else "status-failed"}">{escape(metrics.status)}</div>
        </div>
        <div class="card">
            <div class="card-title">Health Status</div>
            <div class="card-value {"status-success" if report.health_status.lower() == "healthy" else "status-failed"}">{escape(report.health_status)}</div>
        </div>
    </div>

    <div class="card" style="margin-bottom: 30px;">
        <div class="card-title">Health Message</div>
        <div class="card-value" style="font-weight: normal; font-size: 1em;">{escape(report.health_message)}</div>
    </div>

    <div class="summary">
        <div class="card">
            <div class="card-title">Total Steps</div>
            <div class="card-value">{metrics.total_steps}</div>
        </div>
        <div class="card">
            <div class="card-title">Successful Steps</div>
            <div class="card-value">{metrics.successful_steps}</div>
        </div>
        <div class="card">
            <div class="card-title">Failed Steps</div>
            <div class="card-value">{metrics.failed_steps}</div>
        </div>
        <div class="card">
            <div class="card-title">Artifact Count</div>
            <div class="card-value">{metrics.artifact_count}</div>
        </div>
        <div class="card">
            <div class="card-title">Duration</div>
            <div class="card-value">{f"{metrics.duration_seconds:.2f}s" if metrics.duration_seconds is not None else "N/A"}</div>
        </div>
    </div>

    {failed_steps_html}

</body>
</html>
"""
        return html_content
