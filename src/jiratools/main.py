import sys

import rich_click as click

from jiratools.clone_tickets import clone_jira_tickets
from jiratools.transition_tickets import transition_jira_tickets

# Ensure UTF-8 encoding on Windows to handle type hints in help text
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]


@click.group()
def cli():
    pass


@cli.command()
@click.option("--user", default=None, help="JIRA username (defaults to environment variable)")
@click.option("--password", default=None, help="JIRA password (defaults to environment variable)")
@click.option("--jql", default='"filter"="22379" and "status" = "Design"', help="JQL query")
@click.option("--project", default="COTTMODERN", help="Project name")
@click.option("--issue-type", default="Task", help="Issue type")
@click.option("--assignee", default="aa_postponed", help="Assignee")
@click.option(
    "--endpoint",
    default="https://jira.btmd.ru/rest/structure/1.0/structure/104/forest",
    help="JIRA endpoint URL",
)
def clone(  # noqa: PLR0913
    user: str | None,
    password: str | None,
    jql: str,
    project: str,
    issue_type: str,
    assignee: str,
    endpoint: str,
) -> None:
    """Clone JIRA tickets based on the provided parameters."""
    clone_jira_tickets(user, password, jql, project, issue_type, assignee, endpoint)


@cli.command()
@click.option("--user", default=None, help="JIRA username (defaults to environment variable)")
@click.option("--password", default=None, help="JIRA password (defaults to environment variable)")
@click.option("--project", default="COTTMODERN", help="Project name")
@click.option("--transition", default="In Review", help="Transition name")
def transition(
    user: str | None,
    password: str | None,
    project: str,
    transition_name: str,
) -> None:
    """Transition JIRA tickets based on specific logic."""
    transition_jira_tickets(user, password, project, transition_name)


if __name__ == "__main__":
    cli()
