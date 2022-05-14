from board import Board
if __name__ == "__main__":
    game = Board()
    game.refresh_board()
    while True:
        game.drop_char(int(input("Whats your move P1?\n")), 1)
        game.drop_char(int(input("Whats your move P2?\n")), 2)