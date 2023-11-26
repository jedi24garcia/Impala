#!/usr/bin/env python3

#CLASSES


import random

class Student:
  def __init__(self, firstname="", lastname="", email="", campus=""): 
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.campus = campus

  def student_info(self):
    print("Enter the student details")
    self.firstname = input("First Name: ")
    self.lastname = input("Last Name: ")
    self.email = input("Email Address: ")
    self.campus = input("Campus: ")

  def __str__(self):
    return "{} {} {} {}".format(
      self.firstname,
      self.lastname,
      self.email,
      self.campus,
    )
