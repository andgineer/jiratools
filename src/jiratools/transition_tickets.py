from jiratools.config import initialize_jira


def transition_jira_tickets(
    user: str | None,
    password: str | None,
    project: str,
    transition_name: str,
) -> None:
    jira = initialize_jira(user, password)

    issues = jira.search_issues(f'project = {project} AND status = "In Progress"')

    for issue in issues:
        print(f'Transitioning issue {issue.key} to "{transition_name}"')

        # Fetch available transitions for the issue
        transitions = jira.transitions(issue)
        transition_id = None

        # Find the transition ID for the specified transition name
        for transition in transitions:
            if transition["name"] == transition_name:
                transition_id = transition["id"]
                break

        if transition_id is not None:
            # Perform the transition
            jira.transition_issue(issue, transition_id)
            print(f'Successfully transitioned issue {issue.key} to "{transition_name}"')
        else:
            print(f'Error: Transition "{transition_name}" not found for issue {issue.key}')

        # for link in issue.fields.issuelinks:
        #     linked = link.outwardIssue if hasattr(link, 'outwardIssue') else link.inwardIssue
        #     if (linked.fields.status.name == 'Open' and linked.key.startswith('COTTMODERN-')):
        #         if hasattr(linked.fields, 'labels'):
        #             labels = linked.fields.labels
        #         else:
        #             labels = []
        #         linked.update(fields={'labels': labels + ['move2cott']})
        #         print(linked.key)

    print("Transition complete.")
