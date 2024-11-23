import requests

BASE_URL = "http://www.omdbapi.com/"
from conftest import API_KEY

def test_movie_plot_keywords():
    """Test searching for specific keywords in the plot."""
    response = requests.get(BASE_URL, params={"apikey": API_KEY, "t": "Interstellar"})
    assert response.status_code == 200
    data = response.json()
    assert data["Response"] == "True", "Movie not found!"

    plot = data["Plot"].lower()
    assert "space" in plot, "Keyword 'space' missing in plot"
    assert "earth" in plot, "Keyword 'earth' missing in plot"
    assert "planet" in plot, "Keyword 'planet' missing in plot"
