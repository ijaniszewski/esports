from dataclasses import dataclass, field
import glob
import os
import pandas as pd
from typing import List


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
        print(concatenated_df.head())
        # return concatenated_df
    


comments_data = {
    "first_file": "comments-00.csv",
    "files_pattern": "comments-*.csv",
    "col_names": [
        "id_comment",
        "user",
        "id_movie"
        ],
    "index_col": "id_comment"
}

id = IngestData(**comments_data)
id.get_df()



