"""CI/CD Integration Examples"""

GITHUB_ACTIONS = """
name: Validate
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install -r requirements.txt
      - run: python ci_validator_cli.py validate ./configs/ --fail-on-high-risk
"""

GITLAB_CI = """
validate:
  script:
    - pip install -r requirements.txt
    - python ci_validator_cli.py validate ./configs/ --fail-on-high-risk
"""

JENKINS = """
pipeline {
    agent any
    stages {
        stage("Validate") {
            steps {
                sh "python ci_validator_cli.py validate ./configs/ --fail-on-high-risk"
            }
        }
    }
}
"""