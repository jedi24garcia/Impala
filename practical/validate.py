#!/usr/bin/env python3

"""
expression = "abc"
x = "Y"
y = "N"

while True:
  user = input("Enter your expression: ")
  if user == expression:
    break
  else:
    if user is not expression:
      print("try again")
"""
"""
def ExpValidator(UserExpression):
 overview = []
"""

#def is_valid_expression(expression, open_char, close_char):
def valid_expression(UserExpression, open_char, close_char):
  stack = Stack() # creating the stack      
  for char in UserExpression:
    if char == open_char:
      count += 1
    elif char == close_char:
      count -= 1
      
  if count < 0:    
    return False
    
    return stack == 0

def prime():
  print("Welcome to the expression validating program.")
  
  while True:
    # expression from the user
    UserExpression = input(f"Enter your expression: ")
    # open and close brackets
    opening_bracket = input(f"Enter the opening brackets: ")
    closing_bracket = input(f"Enter the closing brackets: ")

    user_redo = input("Do you want to try again? (Y/N): ")
    if user_redo.upper() != "Y":
      print("Bye Bye!!")
      break 

if __name__ == "__prime__":
  print(prime)

#check brackets.py and stack_1.py files on course for guide
