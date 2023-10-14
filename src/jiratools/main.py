import click
from jiratools.clone_tickets import clone_jira_tickets
from jiratools.transition_tickets import transition_jira_tickets


@click.group()
def cli():
    pass


@cli.command()
@click.option('--user', default=None, help='JIRA username (defaults to environment variable)')
@click.option('--password', default=None, help='JIRA password (defaults to environment variable)')
@click.option('--jql', default='"filter"="22379" and "status" = "Design"', help='JQL query')
@click.option('--project', default='COTTMODERN', help='Project name')
@click.option('--issue-type', default='Task', help='Issue type')
@click.option('--assignee', default='aa_postponed', help='Assignee')
@click.option('--endpoint', default='https://jira.btmd.ru/rest/structure/1.0/structure/104/forest', help='JIRA endpoint URL')
def clone(user, password, jql, project, issue_type, assignee, endpoint):
    """Clone JIRA tickets based on the provided parameters."""
    clone_jira_tickets(user, password, jql, project, issue_type, assignee, endpoint)


@cli.command()
@click.option('--user', default=None, help='JIRA username (defaults to environment variable)')
@click.option('--password', default=None, help='JIRA password (defaults to environment variable)')
@click.option('--project', default='COTTMODERN', help='Project name')
@click.option('--transition', default='In Review', help='Transition name')
def transition(user, password, project, transition_name):
    """Transition JIRA tickets based on specific logic."""
    transition_jira_tickets(user, password, project, transition_name)


if __name__ == "__main__":
    cli()
