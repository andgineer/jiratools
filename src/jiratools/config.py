import os

from jira import JIRA

server: str = "https://jira.btmd.ru"


def initialize_jira(user: str | None, password: str | None) -> JIRA:
    jira_username = user or os.getenv("JIRA_USERNAME")
    jira_password = password or os.getenv("JIRA_PASSWORD")

    if not jira_username or not jira_password:
        raise ValueError("JIRA_USERNAME and JIRA_PASSWORD environment variables are not set")

    return JIRA(server=server, options={"verify": False}, basic_auth=(jira_username, jira_password))
