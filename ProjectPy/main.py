#!/usr/bin/env python3

#MAIN

import sys
from classes import Student
from utilities import utility, Menu

def main():
  student_file_name = "student_data.txt"
  student_file_size = 500
  utilities = utility()
  # student = utilities.student_data_file(student_file_name, student_file_size)
  # students = (student_file_name, student_file_size)

  menu = Menu()

  # student_attributes_list = ['firstname', 'lastname', 'email', 'campus']

# calls the main function
if __name__ == "__main__":
  print("**** Welcome TO WHITECLIFFE College of Information Technology ****")
  print("******************** STUDENT PORTAL *************************")
  main()
  sys.exit(0)
