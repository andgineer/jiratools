from jira import JIRA
from password import password
from collections import Counter
from config import server

options = {
    'server': server
}
jira = JIRA(options, basic_auth=('sorokin', password))    # a username/password tuple

# props = jira.application_properties()

issues = jira.search_issues('filter=22379 AND "assignee" = "Андрей Сорокин" AND "status" = "Design"')

# Find the top three projects containing issues reported by admin
top_three = Counter(
    [issue.fields.project.key for issue in issues]).most_common(3)
