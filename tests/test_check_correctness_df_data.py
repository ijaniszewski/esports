# pylint: disable=C0103

"""Test to check if data in dataframes is correct."""

import pandas as pd
import numpy as np
import pytest

from src.main import GetInfo
from tests.test_get_info_from_df import create_movies_example_df


def create_comments_df_with_wrong_data():
    """Create example comments df with wrong data."""
    data = {
        "id_comment": list(range(6)),
        "user": [f"user{user_no}" for user_no in range(6)],
        "id_movie": [1 for no in range(5)] + ["bum"]
    }
    example_df = pd.DataFrame(data, columns = data.keys()).set_index("id_comment")
    return example_df


def create_movies_df_with_wrong_data():
    """Create example movies df with wrong data."""
    data = {
        "id_movie": list(range(6)),
        "title": [f"user{user_no}" for user_no in range(6)],
        "id_game": [1 for no in range(5)] + ["bum"]
    }
    example_df = pd.DataFrame(data, columns = data.keys()).set_index("id_movie")
    return example_df


def assert_df_with_wrong_data(example_df, type_, df_name, col_name):
    """Test check_correctness_of_data method."""
    get_info = GetInfo()
    error_info = (f"There are other types than {type_} in dataframe "
                  f"{df_name} in column {col_name}. Cannot process.")

    with pytest.raises(ValueError) as e:
        get_info.check_correctness_of_data(example_df, col_name, type_, df_name)
    assert str(e.value) == error_info


def test_comments_df_with_wrong_data():
    """Test check_correctness_of_data method for comments df if data is not correct."""
    example_df = create_comments_df_with_wrong_data()
    assert_df_with_wrong_data(example_df, np.int64, "comments_df", "id_movie")


def test_movies_df_with_wrong_data():
    """Test check_correctness_of_data method for movies df if data is not correct."""
    example_df = create_movies_df_with_wrong_data()
    assert_df_with_wrong_data(example_df, np.int64, "movies_df", "id_game")

def test_movies_df_with_correct_data():
    """Test check_correctness_of_data method for movies df if data is correct."""
    example_df = create_movies_example_df()
    get_info = GetInfo()
    correct = get_info.check_correctness_of_data(example_df, "id_game", np.int64, "movies_df")
    assert correct is None
