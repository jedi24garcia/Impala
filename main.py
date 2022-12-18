#!/usr/bin/env python3

from random import randint

print("Let's play fucking Battleship!")

Hidden_Pattern = [[' ']*8 for x in range(6)]
Guess_Pattern = [[' ']*8 for x in range(6)]

"""
board = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
]
"""

let_to_num = {'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5}

def print_board(board):
  print('A B C D E F')
  print('*****')
  row_num = 1
  for row in board:
    print("%d|%s|" % (row_num, "I".join(row)))
    row_num +=1

for n in range(6):
  print("Where you want ship ", n + 1, "?")
  column = input("column (A to F):")
  row = input("row (1 to 6):")
  column_number = let_to_num[column]
  row_number = int(row) - 1

# TODO: need to print board
