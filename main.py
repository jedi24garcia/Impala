#!/usr/bin/env python3

from random import randint

print("Let's play fucking Battleship!")

board = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
]

letters_to_numbers = {
  'A': 0,
  'B': 1,
  'C': 2,
  'D': 3,
  'E': 4,
}

for row in board:
  print(row)

