import pandas as pd
import textwrap


class Loader:
    def __init__(self):
        df = pd.read_csv("sudoku.csv")
        self.games: pd.Series = df.quizzes

    def get_games_count(self) -> int:
        return self.games.count()

    def get_game(self, game: int) -> list[list[int]]:
        game = self.games.get(game)
        return [[int(char) for char in row] for row in textwrap.wrap(game, 9)]


if __name__ == "__main__":
    loader = Loader()
    print(loader.get_game(1))
