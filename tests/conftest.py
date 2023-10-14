import pytest
from unittest.mock import MagicMock, patch
import os


@pytest.fixture
def mock_jira():
    with patch("jiratools.clone_tickets.initialize_jira", return_value=MagicMock()) as mock:
        # Mock the environment variables
        with patch.dict(os.environ, {"JIRA_USERNAME": "your_username", "JIRA_PASSWORD": "your_password"}):
            # Mock the search_issues method
            mock_issue = MagicMock(key="TEST-123", fields=MagicMock(description="Test description", summary="Test summary"))
            mock_issue.id = "123456"  # Make sure the id is a string, which is JSON-serializable

            mock.return_value.search_issues.return_value = [mock_issue]

            # Mock the create_issue method to return another issue with a JSON-serializable id
            mock_new_issue = MagicMock()
            mock_new_issue.key = "NEW-123"
            mock_new_issue.id = "654321"
            mock.return_value.create_issue.return_value = mock_new_issue

            yield mock()  # we want the MagicMock() that is returned by the patched initialize_jira()
