"""Test if IngestData concatenates data properly."""

from src.settings import comments_data, movies_data
from src.main import IngestData


def test_comments_concatenate():
    """Test if comments dataframe is concatenated by get_df method properly."""
    com_id = IngestData(**comments_data)
    comments_df = com_id.get_df()
    assert comments_df.shape[0] > 160000
    assert comments_df.shape[1] == 2


def test_movies_concatenate():
    """Test if movies dataframe is concatenated by get_df method properly."""
    com_id = IngestData(**movies_data)
    movies_df = com_id.get_df()
    assert movies_df.shape[0] > 200
    assert movies_df.shape[1] == 2
