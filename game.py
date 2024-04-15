from board import Board
from game_loader import Loader
import random as rd


class Game:
    def __init__(self):
        self.running = None
        self.board = Board()
        self.loader = Loader()
        self.init()
        
    def init(self):
        self.board.set_board(self.loader.get_game(rd.randint(0, self.loader.get_games_count()-1)))
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.__update()

        print("You win!")

    def __update(self):
        self.board.print_board()
        if self.board.verify_board():
            self.running = False
            return

        inp = input("Enter num col and row (num col row): \n")
        inputs = inp.split(" ")[:3]
        try:
            if len(inputs) == 3:
                num, col, row = list(map(int, inputs))
            else:
                num, col, row = [int(num) for num in str(inputs[0])]
        except ValueError:
            print("Numbers must be numbers")
            return
        for number in [col, row]:
            if not number or number > 9:
                print("Coordinate numbers must be 1-9")
                return
        if num > 9:
            print("Number placed must be 0-9")
            return
        col -= 1
        row -= 1
        self.board.place_square(num, col, row)


if __name__ == "__main__":
    game = Game()
    game.start()
