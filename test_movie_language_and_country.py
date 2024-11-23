import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_movie_language_and_country():
    """Test validating movie language and country."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "Amélie"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "True", "Movie not found!"
    assert "French" in data["Language"], "Language mismatch"
    assert data["Country"] == "France, Germany", "Country mismatch"
