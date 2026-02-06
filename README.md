# CI Pipeline Intelligent Validator

ML-powered pre-execution validation for CI/CD pipelines.

## Quick Start

Install dependencies:
    pip install -r requirements.txt

Validate a directory:
    python ci_validator_cli.py validate ./configs/

Quick check a file:
    python ci_validator_cli.py check config.json

## Python API

Single file validation:
    result = validator.validate_file("config.json")

Directory validation:
    result = validator.validate_directory("./configs/")

Full pipeline:
    result = orchestrator.run_validation("./configs/", fail_on_high_risk=True)

Quick safety check:
    is_safe = orchestrator.quick_check("config.json")

## Risk Levels

| Level  | Score  | Action  |
|--------|--------|---------|
| LOW    | 0-30   | PROCEED |
| MEDIUM | 31-60  | REVIEW  |
| HIGH   | 61-100 | STOP    |

## Project Structure

ci_validator/
  config.json          - Configuration
  pipeline.py          - Main module
  ci_validator_cli.py  - CLI interface
  requirements.txt     - Dependencies
  data/                - Datasets
  models/              - Trained ML models
  reports/             - Generated reports

## License

MIT License