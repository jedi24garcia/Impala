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

class ship

class Ocean



let_to_num = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}

def print_board(board):
  print('a b c d e f')
  print('*****')
  row_num = 1
  for row in board:
    print("%d|%s|" % (row_num, "I".join(row)))
    row_num +=1

for n in range(6):
  print("Where do you want the ship bro ", n + 1, "?")
  column = input("column (a to f):")
  row = input("row (1 to 6):")
  column_number = let_to_num[column]
  row_number = int(row) - 1

# TODO: need to print board
