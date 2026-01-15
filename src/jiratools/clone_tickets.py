import json

from jiratools.config import initialize_jira


def clone_jira_tickets(  # noqa: PLR0913
    user: str | None,
    password: str | None,
    jql: str,
    project: str,
    issue_type: str,
    assignee: str,
    endpoint: str,
) -> None:
    jira = initialize_jira(user, password)

    issues = jira.search_issues(jql)  # type: ignore[bad-assignment]

    for issue in issues:
        print(issue.key)  # type: ignore[missing-attribute]
        description = issue.fields.description or ""  # type: ignore[missing-attribute]

        # Create a new issue based on provided parameters
        new_issue = jira.create_issue(
            project=project,
            summary=issue.fields.summary,  # type: ignore[missing-attribute]
            description=description,
            issuetype={"name": issue_type},
            assignee={"name": assignee},
        )

        # Create a link between the original and cloned issues
        jira.create_issue_link("Links", issue.key, new_issue.key)  # type: ignore[missing-attribute]
        data = {
            "base": 0,
            "root": 0,
            "actions": [
                {
                    "action": "add",
                    "issue": new_issue.id,
                    "under": issue.id,  # type: ignore[missing-attribute]
                    "after": 0,
                },
            ],
        }
        jira._session.post(endpoint, data=json.dumps(data))  # noqa: SLF001

    print("Done.")
