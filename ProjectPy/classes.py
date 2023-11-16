#!/usr/bin/env python3

import random
#import faker

class Students:
  def __init__(self):
    self.firstname = " "
    self.lastname = " "
    self.email = " "
    self.campus = " "

  def StudentInfo(self):
    print("Enter the student details")
    self.firstname = input("First Name: ")
    self.lastname = input("Last Name: ")
    self.email = input("Email Address: ")
    self.campus = input("Campus: ")

# print("**** Welcome TO WHITECLIFFE College of Information Technology ****")
# print("******************** STUDENT PORTAL *************************")
