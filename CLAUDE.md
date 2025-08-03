# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Setup

Use the activation script to set up the development environment:
```bash
. ./activate.sh
```

This script:
- Creates a virtual environment using UV (Astral's UV package manager)
- Installs dependencies from requirements.txt
- Installs the package in development mode

## Commands

### Core Application
```bash
jiratools --help                    # Show main help
jiratools clone --help              # Show clone command options
jiratools transition --help         # Show transition command options
```

### Testing
```bash
pytest -v --cov=src/ --cov-report=xml tests    # Run tests with coverage
pytest tests/                                  # Run all tests
pytest tests/test_clone_tickets.py             # Run specific test file
```

### Code Quality
```bash
pre-commit run --all-files          # Run all pre-commit hooks
ruff check src/                     # Lint source code
ruff format src/                    # Format source code
mypy src/                          # Type checking
```

## Architecture

### Package Structure
- `src/jiratools/` - Main package
  - `main.py` - CLI entry point using rich-click
  - `config.py` - JIRA connection configuration
  - `clone_tickets.py` - Ticket cloning functionality
  - `transition_tickets.py` - Ticket transition functionality

### Authentication
JIRA authentication uses environment variables:
- `JIRA_USERNAME` - JIRA username
- `JIRA_PASSWORD` - JIRA password

Default server: `https://jira.btmd.ru`

### CLI Structure
The application uses rich-click for the CLI with two main commands:
- `clone` - Clone JIRA tickets with customizable JQL queries
- `transition` - Transition tickets based on project and transition name

### Testing Framework
- Uses pytest with unittest.mock for mocking JIRA API calls
- Test fixtures in `tests/conftest.py` provide mock JIRA instances
- Coverage reports generated in XML format for CI integration

### Code Quality Tools
- Ruff for linting and formatting (line length: 100 chars for src, 99 for tests)
- MyPy for type checking (excludes tests directory)
- Pre-commit hooks enforce code quality standards
- Comprehensive ruff rules including security, complexity, and style checks
