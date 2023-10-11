#!/usr/bin/env python3

import os

print("Welcome to the expression validating program.")

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

def ExpValidator():
  print("hello")

ExpValidator()
