#!/usr/bin/env python3

#MAIN

import sys
from classes import Student
from utilities import utility, Menu

def main():
  student_file_name = "student_data.txt"
  student_file_size = 500
  utilities = utility()
  students = utilities.student_data_file(student_file_name, student_file_size)
  # students = (student_file_name, student_file_size)

  menu = Menu()

  while True:
    choice = menu.main_menu()
    if choice == 1:
      student = Student()
      student.student_info()
      students.append(student)
      # students_list_modified = True
      print("New student added")
    if choice == 5:
      print("Thanks")
      break
 

# calls the main function
if __name__ == "__main__":
  print("**** Welcome TO WHITECLIFFE College of Information Technology ****")
  print("******************** STUDENT PORTAL *************************")
  main()
  sys.exit(0)
