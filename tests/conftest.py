import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def base_url():
    """Provide the API base URL to any test that asks for it."""
    return BASE_URL