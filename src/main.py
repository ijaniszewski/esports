"""Ingest Data and Get Info from it, based on passed movie ID."""

from dataclasses import dataclass, field
from typing import List
import glob
import os
import pandas as pd
import numpy as np


from src.settings import comments_data, movies_data


@dataclass
class IngestData:
    """Ingest data, create dataframes and concatenate in one df based on passed names."""
    first_file: str
    files_pattern: str
    col_names: List[str]
    index_col: str
    all_files: List = field(default_factory=list)
    data_directory: str = "data"

    def chcek_if_file_exists(self):
        """Check if the firs file with column names exists."""
        if not os.path.isfile(self.first_file):
            raise FileNotFoundError(f"There is no such file: {self.first_file}")

    def create_paths_to_files(self) -> None:
        """Create list of files to ingest as self parameters."""
        self.first_file = (os.path.join(self.data_directory, self.first_file))
        self.chcek_if_file_exists()
        self.all_files = glob.glob(os.path.join(self.data_directory, self.files_pattern))

    def get_df(self) -> pd.DataFrame:
        """Create concatenated df from path to files.

        Return
        ----------
        concatenated_df: pd.DataFrame
            Concatenated dataframe from all of given csv files.
        """
        self.create_paths_to_files()
        df_from_each_file = (
            pd.read_csv(f, names=self.col_names, index_col=self.index_col)
            if f != self.first_file
            else pd.read_csv(self.first_file, index_col=self.index_col)
            for f in self.all_files)
        concatenated_df = pd.concat(df_from_each_file)
        return concatenated_df


class GetInfo:
    """Load dataframes and get info from it."""
    @staticmethod
    def get_dfs() -> (pd.DataFrame, pd.DataFrame):
        """Load dataframes via IngesData class.

        Return
        ----------
        comments_df: pd.DataFrame
            concatenated dataframe from all comments csv files
        movies_df: pd.DataFrame
            concatenated dataframe from all movies csv files
        """
        com_id = IngestData(**comments_data)
        comments_df = com_id.get_df()
        mov_id = IngestData(**movies_data)
        movies_df = mov_id.get_df()
        return comments_df, movies_df

    @staticmethod
    def get_movie_title(movie_id: int, movies_df: pd.DataFrame) -> str:
        """Return movie title based on given movie_id and dataframe.

        Parameters
        ----------
        movie_id: int
            movie_id as an integer to get it's movie ID
        movies_df: pd.DataFrame
            dataframe to be searched

        Return
        ----------
        title: str
            title of searched movie. If there is no such ID - return None
        """
        try:
            title = movies_df.loc[movie_id]["title"]
            return title
        except KeyError:
            return None

    @staticmethod
    def get_movie_comments(movie_id: int, comments_df: pd.DataFrame) -> int:
        """Return number of comments based on given movie_id and dataframe.

        Parameters
        ----------
        movie_id: int
            movie_id as an integer to get it's number of comments
        movies_df: pd.DataFrame
            dataframe to be searched

        Return
        ----------
        comments_no: int
            comments number of searched movie. If there is no such ID - return 0
        """
        comments_no = comments_df[comments_df["id_movie"]==movie_id].sum()["id_movie"]
        return int(comments_no)

    @staticmethod
    def check_correctness_of_data(dataframe, col_name, type_, df_name):
        """Check if values in a column are as expected in a given dataframe."""
        unique_values = dataframe[col_name].unique()
        correct = all(isinstance(x, type_) for x in list(unique_values))
        if not correct:
            error_info = (f"There are other types than {type_} in dataframe "
                          f"{df_name} in column {col_name}. Cannot process.")
            raise ValueError(error_info)


    def main(self, movie_id: int) -> None:
        """Print title and comments number based on given movie ID.

        Parameters
        ----------
        movie_id: int
            movie_id as an integer to get it's title and number of comments
        """
        comments_df, movies_df = self.get_dfs()
        self.check_correctness_of_data(comments_df, "id_movie", np.int64, "comments_df")
        self.check_correctness_of_data(movies_df, "id_game", np.int64, "movies_df")
        title = self.get_movie_title(movie_id, movies_df)
        comments_no = self.get_movie_comments(movie_id, comments_df)
        if title is None:
            print(f"There is no title for movie ID you provided: {movie_id}")
        else:
            if comments_no == 0:
                comments_text = "are no comments"
            elif comments_no == 1:
                comments_text = "is one comment"
            else:
                comments_text = f"are {comments_no} comments"
            print(f"There {comments_text} for the movie: {title} (movie ID: {movie_id}).")
