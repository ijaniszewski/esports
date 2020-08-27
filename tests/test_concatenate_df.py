import pandas as pd

from src.settings import comments_data, movies_data
from src.main import IngestData



def test_comments_concatenate():
    com_id = IngestData(**comments_data)
    comments_df = com_id.get_df()
    assert comments_df.shape[0] > 1000
    assert comments_df.shape[1] == 4
