#!/usr/bin/env python3

class UserValidator:
  def __init__(self, opening_bracket, closing_bracket):
    self.stack = []
    self.opening_bracket = opening_bracket
    self.closing_bracket = closing_bracket

  def valid_expression(self, UserExpression):
    self.stack = [] # creating the stack
    self.UserExpression = UserExpression      
    for char in self.UserExpression:
      if char == self.opening_bracket:
        self.stack.append(char)
      elif char == self.closing_bracket:
        if not self.stack:
          return False
        if self.stack[-1] == self.opening_bracket:
          self.stack.pop()
        else:
          return False
      
    return len(self.stack) == 0

def main():
  print("Welcome to the expression validating program.")
  
  while True:
    try:  
    # expression from the user
      UserExpression = input(f"Enter your expression: ")
    except (NameError, KeyboardInterrupt):
      raise SystemExit 
    # open and close brackets
    opening_bracket = input(f"Enter the opening brackets: ")
    closing_bracket = input(f"Enter the closing brackets: ")

    validator = UserValidator(opening_bracket, closing_bracket)
    
    if validator.valid_expression(UserExpression):
      print("Valid Expression.\n")
    else:
      print("Invalid Expression.\n")
   
    user_redo = input("Do you want to try again? (Y/N): ")
    if user_redo.upper() != "Y":
      print("Bye Bye!!")
      break 

if __name__ == "__main__":
  main()

# 1. Why did you select that specific data structure?
# This structure allows users to enter an expression and would validate that expression if its valid or not. 
# A stack is the data structure used in this program. I chose this structure as it allows for an
# efficient checking of matching brackets in an expression. 
# 2. How was that data structure suited to the task?
# The stack data structure suited the task as the structure is well-suited to efficiently track
# and authenticate bracket pairs in expressions. This is what requires in the task for validating expressions with matching brackets.
# 3. Could another data structure be used to complete the same task? If so, how would your solution differ?
# Yes, you can use queue data structure however it may result to less efficient. I believe stack
# is more straightforward and more efficient.