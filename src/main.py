from dataclasses import dataclass, field
import glob
import os
import pandas as pd
from typing import List

from src.settings import comments_data, movies_data


@dataclass
class IngestData:
    first_file: str
    files_pattern: str
    col_names: List[str]
    index_col: str
    all_files: List = field(default_factory=list)
    data_directory: str = "data"

    def create_paths_to_files(self):
        self.first_file = (os.path.join(self.data_directory, self.first_file))
        self.all_files = glob.glob(os.path.join(self.data_directory, self.files_pattern))

    def get_df(self):
        self.create_paths_to_files()
        df_from_each_file = (pd.read_csv(f, names=self.col_names, index_col=self.index_col) if f != self.first_file else pd.read_csv(self.first_file, index_col=self.index_col) for f in self.all_files)
        concatenated_df = pd.concat(df_from_each_file)
        return concatenated_df


class GetInfo:
    def get_dfs(self):
        com_id = IngestData(**comments_data)
        comments_df = com_id.get_df()
        mov_id = IngestData(**movies_data)
        movies_df = mov_id.get_df()
        return comments_df, movies_df

    def get_movie_title(self, movie_id, movies_df):
        try:
            title = movies_df.loc[movie_id]["title"]
            return title
        except KeyError:
            return None

    def get_movie_comments(self, movie_id, comments_df):
        comments_no = comments_df[comments_df["id_movie"]==movie_id].sum()["id_movie"]
        return comments_no

    def main(self, movie_id):
        comments_df, movies_df = self.get_dfs()
        title = self.get_movie_title(movie_id, movies_df)
        comments_no = self.get_movie_comments(movie_id, comments_df)
        if title is None:
            print(f"There is no title for id movie you provided: {movie_id}")
        else:
            print(f"There is {comments_no} comments for the movie: {title} (movie ID: {movie_id}).")
        
