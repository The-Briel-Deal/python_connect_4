import os
from typing import List

class Board:
    def __init__(self) -> None:
        self.matrix: List = [[0 for i2 in range(10)] for i1 in range(10)]
    def refresh_board(self) -> None:
        os.system("clear")
        for row in self.matrix:
            print(row)
    def drop_char(self,row: int, num: int) -> None:
        self.matrix[0][row] = num
        self.refresh_board()