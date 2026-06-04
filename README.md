# Open Data Lakehouse Lab: Dashboards

The dashboards repository is responsible for local dashboard foundations within the Open Data Lakehouse Lab project.

## Purpose

The repository provides lightweight, local static dashboard generation from observability reports. It aims to provide a simple way to visualize the status of data pipelines and workflows without requiring complex infrastructure or external services during the initial phase.

## Current Scope

- Read local observability JSON reports.
- Render simple standalone static HTML dashboards.
- CLI-based dashboard generation (`odl-dashboards`).
- Tests without network access or external services.

## Installation

### Prerequisites

- Python 3.12+

### Setup

```bash
# Clone the repository and navigate to it
cd dashboards

# Create a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install development dependencies
python3 -m pip install -r requirements-dev.txt

# Install the package in editable mode
python3 -m pip install -e .
```

## Usage

### CLI

The `odl-dashboards` command is exposed after installation.

#### Version

```bash
odl-dashboards version
```

#### Render Dashboard

```bash
odl-dashboards render observability \
  --report-path ./examples/run-observability-report.json \
  --output-dir ./dashboard
```

This will generate an `index.html` file in the specified output directory.

## Validation

To run linting and tests:

```bash
bash scripts/validate.sh
```

## Documentation

- [Dashboard Design](docs/dashboard-design.md)
- [Local Static Dashboard](docs/local-static-dashboard.md)
- [Future Dashboard Tools](docs/future-dashboard-tools.md)

## License

Unless otherwise noted:

- Software, scripts, Infrastructure as Code, SQL models, configuration files and executable assets are licensed under the [Apache License 2.0](LICENSE).
- Documentation, diagrams and written content are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Original upstream datasets, when referenced, remain governed by their original source licenses and terms.
