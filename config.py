from jira import JIRA
from password import password

server='https://jira.btmd.ru'
jira = JIRA(server=server, options={'verify': False}, basic_auth=('sorokin', password))
