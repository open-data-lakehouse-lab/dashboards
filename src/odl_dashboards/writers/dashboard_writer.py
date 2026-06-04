from pathlib import Path
from ..utils.paths import ensure_dir

class DashboardWriter:
    def write(self, html_content: str, output_dir: Path) -> Path:
        ensure_dir(output_dir)
        output_path = output_dir / "index.html"
        with open(output_path, "w") as f:
            f.write(html_content)
        return output_path
