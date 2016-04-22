from config import jira

issues = jira.search_issues('filter=22379')

for issue in issues:
    # new_issue = jira.create_issue(project='COTTMODERN', summary=issue.fields.summary,
    #                               description=issue.fields.description, issuetype=issue.fields.issuetype)
    # jira.create_issue_link({'name': 'Link'}, {'key', issue.key}, {'key', new_issue.key})
    for link in issue.fields.issuelinks:
        linked = link.outwardIssue if hasattr(link, 'outwardIssue') else link.inwardIssue
        if (linked.fields.status.name == 'Open'
             and linked.key.startswith('COTTMODERN-')):
            print(linked.key)
