# AIForTesting - PyPI UI Automation (BDD + Selenium)

This project contains functional UI test automation for [PyPI](https://pypi.org) using:
- Python
- Pytest
- Pytest-BDD (Gherkin)
- Selenium WebDriver
- Page Object Model

The suite focuses on the 5 highest-priority user journeys for package discovery and account entry points.

## Covered Test Scenarios

1. Home page loads core controls.
2. Search returns results for a known package.
3. Opening package details from search works.
4. Release history is accessible from package page.
5. Login page shows required controls.

Feature file: `tests/features/pypi_ui.feature`

## Project Structure

```text
.
├── pytest.ini
├── requirements.txt
└── tests
    ├── conftest.py
    ├── features
    │   └── pypi_ui.feature
    ├── pages
    │   ├── base_page.py
    │   ├── home_page.py
    │   ├── search_results_page.py
    │   ├── project_page.py
    │   └── login_page.py
    └── steps
        └── test_pypi_steps.py
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run Tests

Use the venv interpreter explicitly:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q -p pytest_bdd
```

## Configuration

Supported environment variables:
- `PYPI_BASE_URL` (default: `https://pypi.org`)
- `UI_WAIT_TIMEOUT` (default: `15` seconds)
- `HEADLESS` (default: `true`)
- `CHROMEDRIVER_PATH` (optional override for local driver binary)

Example:

```bash
HEADLESS=false UI_WAIT_TIMEOUT=20 python -m pytest -q -p pytest_bdd
```

## Design Notes

- No `sleep` calls are used. Synchronization relies on explicit waits (`WebDriverWait` + expected conditions).
- Locators and actions are encapsulated in page objects.
- Base URL and wait timeout are configurable to avoid hardcoding.
- Tests follow Python best practices and readable BDD step definitions.
