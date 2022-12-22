#!/usr/bin/env python3

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
  def __init__(self, board, width, height):
    self.board = board
    self.width = width
    self.height = height











































