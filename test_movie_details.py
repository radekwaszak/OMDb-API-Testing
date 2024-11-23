import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_movie_details():
    """Test fetching detailed movie information."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "The Dark Knight"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "True", "Movie not found!"
    assert data["Released"] == "18 Jul 2008", "Release date mismatch"
    assert data["Runtime"] == "152 min", "Runtime mismatch"
    assert "Action" in data["Genre"], "Genre mismatch"
    assert data["Director"] == "Christopher Nolan", "Director mismatch"
    assert "Joker wreaks havoc" in data["Plot"], "Plot mismatch"
    assert "English" in data["Language"], "Language mismatch"
    assert data["Country"] == "United States, United Kingdom", "Country mismatch"
    assert "Won 2 Oscars" in data["Awards"], "Awards mismatch"
