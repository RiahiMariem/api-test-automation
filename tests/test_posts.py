import pytest
import requests

# Every test function must start with "test_" so pytest can find it.


def test_get_all_posts_returns_200(base_url):
    """The posts list should load successfully."""
    response = requests.get(f"{base_url}/posts", timeout=10)

    # assert checks that something is true. If it is false, the test fails.
    assert response.status_code == 200


def test_get_all_posts_returns_100_items(base_url):
    """The fake API contains exactly 100 posts."""
    response = requests.get(f"{base_url}/posts", timeout=10)
    posts = response.json()

    assert len(posts) == 99


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_single_post(base_url, post_id):
    """Each requested post should return the correct ID and fields."""
    response = requests.get(f"{base_url}/posts/{post_id}", timeout=10)

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == post_id
    assert "title" in body
    assert "body" in body


def test_get_missing_post_returns_404(base_url):
    """Asking for a post that does not exist should return 'Not Found'."""
    response = requests.get(f"{base_url}/posts/9999", timeout=10)

    assert response.status_code == 404


def test_create_post_returns_201(base_url):
    """Sending a new post should return 'Created' with our data."""
    new_post = {"title": "My first test", "body": "Hello from pytest", "userId": 1}

    response = requests.post(f"{base_url}/posts", json=new_post, timeout=10)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == new_post["title"]
    assert body["body"] == new_post["body"]