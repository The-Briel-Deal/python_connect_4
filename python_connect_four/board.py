import os
from typing import List
from time import sleep


class Board:
    def __init__(self) -> None:
        self.matrix: List = [[0 for i2 in range(10)] for i1 in range(10)]

    def refresh_board(self) -> None:
        os.system("clear")
        for row in self.matrix:
            print(f"{row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}  {row[5]}  {row[6]}  {row[7]}  {row[8]}  {row[9]}")
        print(("^  ^  ^  ^  ^  ^  ^  ^  ^  ^\n0  1  2  3  4  5  6  7  8  9"))

    def find_curr_height(self, col):
        curr = len(self.matrix) - 1
        while self.matrix[curr][col] != 0:
            curr -= 1
        return curr

    def drop_char(self, col: int, num: int) -> None:
        self.matrix[0][col] = num
        row = 0
        while True:
            if len(self.matrix)-1 == row or row >= self.find_curr_height(col):
                break
            self.matrix[row+1][col], self.matrix[row][col] = self.matrix[row][col], self.matrix[row+1][col]
            row += 1
            self.refresh_board()
            sleep(.2)
            self.matrix[self.find_curr_height(col)][col] != 0
        if self.check_for_win(row, col):
            os.system("clear")
            print(f'{self.matrix[row][col]} WINS!!!')
            quit()

    def check_for_win(self, row: int, col: int) -> bool:
        num = self.matrix[row][col]
        dirs = [[0, 1], [1, 0], [1, 1], [-1, 1]]
        for dir in dirs:
            in_this_direction = 1
            rp, cp = dir
            col_total = col + cp
            row_total = row + rp
            neg_col_total = col - cp
            neg_row_total = row - rp
            while (row_total >= 0 and 
                   col_total >= 0 and 
                   row_total < len(self.matrix) and 
                   col_total < len(self.matrix[0]) and 
                   self.matrix[row_total][col_total] == num):
                row_total += rp
                col_total += cp
                in_this_direction += 1
            while (neg_row_total >= 0 and 
                   neg_col_total >= 0 and 
                   neg_row_total < len(self.matrix) and 
                   neg_col_total < len(self.matrix[0]) and 
                   self.matrix[neg_row_total][neg_col_total] == num):
                neg_row_total -= rp
                neg_col_total -= cp
                in_this_direction += 1
            if in_this_direction >= 4:
                return True
        return False