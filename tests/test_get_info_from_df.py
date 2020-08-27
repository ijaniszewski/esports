"""Test if getting info from dataframes works properly."""

import pandas as pd

from src.main import GetInfo


def create_comments_example_df():
    """Create example df based on how comments CSV are structured."""
    data = {
        "id_comment": list(range(6)),
        "user": [f"user{user_no}" for user_no in range(6)],
        "id_movie": [1 for no in range(3)] + [2 for no in range(3)]
    }
    example_df = pd.DataFrame(data, columns = data.keys()).set_index("id_comment")
    return example_df


def create_movies_example_df():
    """Create example df based on how movies CSV are structured."""
    data = {
        "id_movie": list(range(6)),
        "title": [f"movie_{movie}" for movie in range(6)],
        "id_game": [1 for no in range(3)] + [2 for no in range(3)]
    }
    example_df = pd.DataFrame(data, columns = data.keys()).set_index("id_movie")
    return example_df


def test_get_movie_comments():
    """Test get movie comments method based on example dataframe."""
    example_df = create_comments_example_df()
    get_info = GetInfo()
    comments_no = get_info.get_movie_comments(1, example_df)
    assert comments_no == 3


def test_get_movie_title():
    """Test get movie title method based on example dataframe."""
    example_df = create_movies_example_df()
    get_info = GetInfo()
    movie_title = get_info.get_movie_title(1, example_df)
    assert movie_title == "movie_1"


def test_get_movie_title_no_movie_id():
    """Test get movie tile method based on example dataframe if there is no such ID."""
    example_df = create_movies_example_df()
    get_info = GetInfo()
    movie_title = get_info.get_movie_title('X', example_df)
    assert movie_title is None
