import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_movie_not_found():
    """Test searching for a non-existent movie."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "NonExistentMovie"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "False"
    assert data["Error"] == "Movie not found!"