from config import initialize_jira
import json


def clone_jira_tickets():
    jira = initialize_jira()

    issues = jira.search_issues('"filter"="22379" and "status" = "Design"')

    for issue in issues:
        print(issue.key)
        descr = issue.fields.description
        t = jira.transitions(issue)
        if not descr:
            descr = ''
        new_issue = jira.create_issue(project='COTTMODERN', summary=issue.fields.summary,
                                      description=descr, issuetype={'name': 'Task'},
                                      assignee={'name': 'aa_postponed'})

        # Uncomment and modify as needed
        # tt = new_issue.fields.timetracking
        # tt.originalestimate='4h'
        # new_issue.update(fields={'timeoriginalestimate': '4h'})

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
        url = 'https://jira.btmd.ru/rest/structure/1.0/structure/104/forest'
        r = jira._session.post(url, data=json.dumps(data))

        # Uncomment and modify as needed
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

    print('Done.')


if __name__ == "__main__":
    clone_jira_tickets()
