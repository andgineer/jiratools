from jiratools import clone_tickets


def test_clone_jira_tickets(mock_jira):
    # Call the function under test
    clone_tickets.clone_jira_tickets()

    # Verify that the search_issues method was called with the correct parameters
    mock_jira.search_issues.assert_called_once_with('"filter"="22379" and "status" = "Design"')

    # Verify that the create_issue method was called
    mock_jira.create_issue.assert_called_once()

    # Verify that the create_issue_link method was called
    mock_jira.create_issue_link.assert_called_once_with('Links', 'TEST-123', 'NEW-123')

    # Verify that the custom API call was made
    mock_jira._session.post.assert_called_once()

