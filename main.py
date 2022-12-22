#!/usr/bin/env pythion3

from random import randint

print("Let's play fucking Battleship!")

Hidden_Pattern = [[' '] *8 for x in range(6)]
Guess_Pattern = [[' '] *8 for i in range(6)]

"""
board = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
]
"""

class Battleboard:
  def __init__(self, board):
    self.board = board
    
class Ocean:
  def view_ocean(self):
    for row in self.ocean:
      print(" ".join(row))


























"""
let_to_num = {'a':0,'b':1,'c':2} # 'd':3,'e':4,'f':5}

def print_board(board):
  print('a b c d e f')
  print('*****')
  row_num = 1
  for row in board:
    print("%d|%s|" % (row_num, "I".join(row)))
    row_num +=1

for n in range(2):
  print("Where do you want the ship bro ", n + 1, "?")
  column = input("column (a to c):")
  row = input("row (1 to 2):")
  column_number = let_to_num[column]
  row_number = int(row) - 1
"""

