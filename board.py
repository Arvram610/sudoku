from copy import deepcopy

def verify_set(square_set: list[int]) -> bool:
    return len(set(square_set)) == len(square_set)


class Board:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.editables = deepcopy(self.board)

    def set_board(self, board: list[list[int]]):
        self.board = board
        self.editables = deepcopy(self.board)

    def get_row(self, row: int) -> list[int]:
        return self.board[row]

    def get_col(self, col: int) -> list[int]:
        return [self.board[i][col] for i in range(9)]

    def get_square(self, square: int) -> list[int]:
        start_x = (square % 3) * 3
        start_y = (square // 3) * 3
        return [self.board[y][x] for y in range(start_y, start_y + 3) for x in range(start_x, start_x + 3)]

    def place_square(self, number: int, col: int, row: int) -> None:
        if not self.editables[row][col]:
            self.board[row][col] = number
        else:
            print("Cannot replace preplaced piece")

    def verify_board(self) -> bool:
        for index in range(9):
            if False in map(verify_set, [self.get_row(index), self.get_square(index), self.get_col(index)]):
                return False
        return True

    def print_board(self):
        for row in range(9):
            row_set = self.get_row(row)
            for col in range(9):
                char: str = str(row_set[col])
                print(char.replace("0", " "), end="")
                if col != 8:
                    seperator = " | "
                    if not (col+1) % 3:
                        seperator = " || "
                    print(seperator, end="")

            if row != 8:
                seperator = "\n-- --- ---  --- --- ---  --- --- ---"
                if not (row + 1) % 3:
                    seperator = seperator.replace("-", "=")
                print(seperator)
        print("")


if __name__ == "__main__":
    board = Board()
    board.print_board()
