from board import Board


class Game:
    def __init__(self):
        self.board = Board()
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
        for number in [num, col, row]:
            if not number or number > 9:
                print("All numbers must be 1-9")
                return
        col -= 1
        row -= 1
        self.board.place_square(num, col, row)


if __name__ == "__main__":
    game = Game()
    game.start()
