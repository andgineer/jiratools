[![Build Status](https://github.com/andgineer/jiratools/workflows/ci/badge.svg)](https://github.com/andgineer/jiratools/actions) [![Coverage](https://raw.githubusercontent.com/andgineer/jiratools/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/andgineer/jiratools/blob/python-coverage-comment-action-data/htmlcov/index.html)

# Jira Automation Tools

A command-line tool for automating Jira workflows, including ticket cloning and status transitions.

## Features

- **Clone Tickets**: Duplicate Jira tickets based on JQL queries with customizable parameters
- **Transition Tickets**: Bulk update ticket statuses across projects

## Installation

### Prerequisites

- Python 3.10 or higher
- [UV package manager](https://github.com/astral-sh/uv) (recommended)

### Setup

1. Set up the development environment:
   ```bash
   . ./activate.sh
   ```

   This script will:
   - Create a virtual environment using UV
   - Install all dependencies
   - Install the package in development mode

2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

3. Verify installation:
   ```bash
   jiratools --help
   ```

## Configuration

Set up your Jira credentials as environment variables:

```bash
export JIRA_USERNAME="your_username"
export JIRA_PASSWORD="your_password"
```

Alternatively, you can pass credentials directly via command-line options.

## Usage

### Basic Commands

```bash
# Show available commands
jiratools --help

# Clone tickets
jiratools clone --help

# Transition tickets
jiratools transition --help
```

### Clone Tickets

Clone tickets based on JQL queries:

```bash
jiratools clone \
  --jql '"filter"="22379" and "status" = "Design"' \
  --project "MYPROJECT" \
  --issue-type "Task" \
  --assignee "john.doe"
```

### Transition Tickets

Update ticket statuses:

```bash
jiratools transition \
  --project "MYPROJECT" \
  --transition "In Review"
```

### Advanced Options

All commands support additional options:

- `--user`: Override default username
- `--password`: Override default password
- `--endpoint`: Custom Jira endpoint URL

## Development

### Running Tests

```bash
# Run all tests with coverage
pytest -v --cov=src/ --cov-report=xml tests

# Run specific test file
pytest tests/test_clone_tickets.py
```

### Code Quality

```bash
# Run linting and formatting
pre-commit run --all-files

# Manual checks
ruff check src/
ruff format src/
mypy src/
```

## License

MIT License - see the LICENSE file for details.
