import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_search_movie():
    """Test searching for a movie by title."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "Guardians of the Galaxy Vol. 2"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "True"
    assert data["Title"] == "Guardians of the Galaxy Vol. 2"

def test_invalid_api_key():
    """Test handling of an invalid API key."""
    response = requests.get(BASE_URL, params={"apikey": "invalid_key", "t": "Guardians of the Galaxy Vol. 2"})
    assert response.status_code in [200, 401], "Unexpected status code"
    if response.status_code == 401:
        assert "Invalid API key" in response.text
    else:
        data = response.json()
        assert data["Response"] == "False"
        assert data["Error"] == "Invalid API key!"
