from odl_dashboards.writers.dashboard_writer import DashboardWriter

def test_write_dashboard(tmp_path):
    writer = DashboardWriter()
    html_content = "<html><body>Test</body></html>"
    output_dir = tmp_path / "dashboard"
    
    generated_path = writer.write(html_content, output_dir)
    
    assert (output_dir / "index.html").exists()
    assert generated_path == output_dir / "index.html"
    assert generated_path.read_text() == html_content

def test_write_creates_output_dir(tmp_path):
    writer = DashboardWriter()
    html_content = "<html><body>Test</body></html>"
    output_dir = tmp_path / "nested" / "dashboard"
    
    writer.write(html_content, output_dir)
    
    assert output_dir.exists()
    assert (output_dir / "index.html").exists()
