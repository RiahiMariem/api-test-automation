![API Tests](https://github.com/RiahiMariem/api-test-automation/actions/workflows/tests.yml/badge.svg)

# API Test Automation

Automated tests for the JSONPlaceholder REST API, written in Python with pytest.

## Features
- Tests for GET, POST, and 404 responses
- HTML and JUnit reports
- GitHub Actions pipeline that runs on every push and pull request

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate it and install dependencies: `pip install -r requirements.txt`

## Run the tests
pytest

## Generate reports
pytest --html=reports/report.html --self-contained-html --junitxml=reports/junit.xml

## Project structure
- `tests/`: test files and shared fixtures
- `.github/workflows/`: CI/CD pipeline definition
- `pytest.ini`: pytest configuration
