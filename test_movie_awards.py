import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_movie_awards():
    """Test checking movie awards and nominations."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "Parasite"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "True", "Movie not found!"
    assert "Won 4 Oscars" in data["Awards"], "Awards data mismatch"
    assert "316 wins & 266 nominations" in data["Awards"], "Awards details mismatch"
