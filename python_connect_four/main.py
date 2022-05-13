from board import Board
if __name__ == "__main__":
    game = Board()
    while True:
        game.drop_char(int(input()), 5)