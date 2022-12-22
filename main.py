#!/usr/bin/env python3

from random import randint
import os

print("Let's play fucking Battleship!")

class battleboard:
  def __init__(self, size):
    self.size = size
