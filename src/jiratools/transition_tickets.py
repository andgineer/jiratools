from jiratools.config import initialize_jira


def transition_jira_tickets(user, password):
    jira = initialize_jira()

    # Fetch issues based on some criteria (example)
    issues = jira.search_issues('project = COTTMODERN AND status = "In Progress"')

    for issue in issues:
        print(f'Transitioning issue {issue.key}')

        # jira.transition_issue(issue, '1')
        # print(r)
        # for link in issue.fields.issuelinks:
        #     linked = link.outwardIssue if hasattr(link, 'outwardIssue') else link.inwardIssue
        #     if (linked.fields.status.name == 'Open' and linked.key.startswith('COTTMODERN-')):
        #         if hasattr(linked.fields, 'labels'):
        #             labels = linked.fields.labels
        #         else:
        #             labels = []
        #         linked.update(fields={'labels': labels + ['move2cott']})
        #         print(linked.key)


    print('Transition complete.')
