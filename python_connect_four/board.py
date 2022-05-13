import os
from typing import List
from time import sleep

class Board:
    def __init__(self) -> None:
        self.matrix: List = [[0 for i2 in range(10)] for i1 in range(10)]
    def refresh_board(self) -> None:
        os.system("clear")
        for row in self.matrix:
            print(row)
    def drop_char(self,col: int, num: int) -> None:
        self.matrix[0][col] = num
        row = 0
        while True:
            if len(self.matrix) >= row-1 and self.matrix[row-1][col] != 0:
                break
            self.matrix[row-1][col], self.matrix[row][col] = self.matrix[row][col], self.matrix[row-1][col]
            self.refresh_board()