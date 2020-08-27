"""Get movie id from passed argument."""

import argparse

from src.main import GetInfo


class GetArgument:
    def get_argument(self):
        """Get the movie id from argument if it is integer.

        Return
        ----------
        movie_id: int
            Movie ID as an integer
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-m',
            '--movie_id',
            help="Please provide movie id as an integer",
            type=int,
            required=True)
        movie_id = parser.parse_args().movie_id
        return movie_id

    def from_file(self):
        """Get the movie_id as passed argument and create GetInfo object."""
        movie_id = self.get_argument()
        gi = GetInfo()
        gi.main(movie_id)


if __name__ == "__main__":
    ga = GetArgument()
    ga.from_file()