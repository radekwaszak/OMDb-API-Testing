import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_runtime_with_invalid_movie():
    """Test checking runtime for a non-existent movie."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "NonExistentMovie123"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "False", "Unexpectedly found a non-existent movie!"
    assert data["Error"] == "Movie not found!", "Error message mismatch"