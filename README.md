# OMDb API Testing

This project tests the OMDb API (Open Movie Database) to ensure its functionality and correctness. The tests cover various aspects of movie data retrieval, including handling valid and invalid requests, movie details, awards, and more.

### Test Cases Created:
1. **`test_api_key.py`**: Validates the functionality of the API key, ensuring that the API responds correctly to requests with a valid key.
2. **`test_movie_awards.py`**: Tests the retrieval of awards and nominations for a specific movie, verifying the accuracy of award information.
3. **`test_movie_details.py`**: Verifies the retrieval of movie details such as release date, runtime, genre, director, plot, language, country, and awards.
4. **`test_movie_language_and_country.py`**: Ensures the correct retrieval of the language and country information for a movie.
5. **`test_movie_plot_keywords.py`**: Searches for specific keywords in a movie's plot to validate its content.
6. **`test_non_existent_movie.py`**: Tests the behavior of the API when a non-existent movie is queried, ensuring that the appropriate error message is returned.
7. **`test_runtime_with_invalid_movie.py`**: Checks the API's response when an invalid movie title is provided, ensuring that a "movie not found" error is returned.

### How to Run the Tests:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the tests:
   ```bash
   pytest --html=report.html

3. The results will be stored in a report file named [report.html](report.html).
