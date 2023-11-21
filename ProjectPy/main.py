#!/usr/bin/env python3

#MAIN

from classes import Students
from utilities import utility
import sys


def main():
  student_file_name = "students.cvs"
  student_file_size = 300
  utilities = utility()
  # students = utilities.student_data_file(student_file_name, student_file_size)
  students = (student_file_name, student_file_size)


# calls the main function
if __name__ == "__main__":
  print("**** Welcome TO WHITECLIFFE College of Information Technology ****")
  print("******************** STUDENT PORTAL *************************")
  main()
  sys.exit(0)
