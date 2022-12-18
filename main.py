#!/usr/bin/env python3

from random import randint

print("Let's play fucking Battleship!")

battleship_board = [
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

for n in range(5):
  print("Where you want ship ", n + 1, "?")
  column = input("column (A to E):")
  row = input("row (1 to 5):")
  column_number = letters_to_numbers[column]
  row_number = int(row) - 1
  
if battleship_board[row_number][column_number] == 'X':
 print('spot is already in used') # if there is a repeat
if column not in "ABCDE":
 print('column is wrong, please use ABCDE only')
if row not in "12345":
 print('row is wrong, please use 12345 only')
  
for row in battleship_board:
  print(row)

