from jira import JIRA
from password import password

server = 'https://jira.btmd.ru'


def initialize_jira():
    return JIRA(server=server, options={'verify': False}, basic_auth=('sorokin', password))
