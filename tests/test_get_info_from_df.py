import pandas as pd

from src.main import GetInfo


def create_comments_example_df():
    data = {
        "id_comment": [no for no in range(6)],
        "user": [f"user{user_no}" for user_no in range(6)],
        "id_movie": [1 for no in range(3)] + [2 for no in range(3)]
    }
    df = pd.DataFrame(data, columns = data.keys()).set_index("id_comment")
    return df


def create_movies_example_df():
    data = {
        "id_movie": [no for no in range(6)],
        "title": [f"movie_{movie}" for movie in range(6)],
        "ig_game": [1 for no in range(3)] + [2 for no in range(3)]
    }
    df = pd.DataFrame(data, columns = data.keys()).set_index("id_movie")
    return df



def test_get_movie_comments():
    example_df = create_comments_example_df()
    gi = GetInfo()
    comments_no = gi.get_movie_comments(1, example_df)
    assert comments_no == 3


def test_get_movie_title():
    example_df = create_movies_example_df()
    gi = GetInfo()
    movie_title = gi.get_movie_title(1, example_df)
    assert movie_title == "movie_1"


def test_get_movie_title_no_movie_id():
    example_df = create_movies_example_df()
    gi = GetInfo()
    movie_title = gi.get_movie_title('X', example_df)
    assert movie_title == None
