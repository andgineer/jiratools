import json
from jiratools.config import initialize_jira


def clone_jira_tickets(user, password, jql, project, issue_type, assignee, endpoint):
    jira = initialize_jira(user, password)

    issues = jira.search_issues(jql)

    for issue in issues:
        print(issue.key)
        description = issue.fields.description or ''

        # Create a new issue based on provided parameters
        new_issue = jira.create_issue(
            project=project,
            summary=issue.fields.summary,
            description=description,
            issuetype={'name': issue_type},
            assignee={'name': assignee}
        )

        # Create a link between the original and cloned issues
        jira.create_issue_link('Links', issue.key, new_issue.key)
        data = {
            "base": 0,
            "root": 0,
            "actions": [
                {
                    "action": "add",
                    "issue": new_issue.id,
                    "under": issue.id,
                    "after": 0
                },
            ]
        }
        r = jira._session.post(endpoint, data=json.dumps(data))

    print('Done.')
