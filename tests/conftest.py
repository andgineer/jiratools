import pytest
from unittest.mock import MagicMock, patch
import sys
import os


# Add the tests directory to the start of sys.path so we will use passwds.py from the tests directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# add project root where is the code we want to test
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_jira():
    with patch("clone_tickets.initialize_jira", return_value=MagicMock()) as mock:
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



