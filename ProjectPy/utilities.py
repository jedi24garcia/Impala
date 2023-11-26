#!/usr/bin/env python3

#UTILITY

import pandas as pd
import os, random
from classes import Student
import csv

class utility():
  def file_exists(self, file_name):
    if os.path.isfile(file_name):
      return True
    else:
      return False

  def student_data_file(self, file_name, file_size):
    if not self.file_exists(file_name):
      print("File does not exist.")
      return []
    else:
      print("File exist.")
      return self.read_student_data_file(file_name)

  def read_student_data_file(self, file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    students = []
    with open(file_name, 'r') as file:
      lines = file.readlines()
      for line in lines:
        data = line.strip().split('\t') 
        students.append(students)
    return students

  # def save_student_data_file(self,file_name,students):
  #     # Convert the list of Student objects into a DataFrame
  #     df = pd.DataFrame([s.__dict__ for s in students])

  #     # Write the DataFrame into a CSV file
  #     df.to_csv(file_name, index=False)

# FUNCTION FOR MAIN MENU

class Menu():
  def main_menu(self):
    print("MAIN MENU")
    print("1. ADD NEW STUDENT")
    print("2. DELETE STUDENT")
    print("3. SHOW STUDENTS")
    print("4. SEARCH STUDENT")
    print("Type EXIT to quit your application")
    user_input = int(input("Enter your choice: "))
    return user_input

# FUNCTION FOR STUDENT ADD MENU

  def student_add_menu():
    student_menu_options = {
      1: "First Name",
      2: "Last Name",
      3: "Email Address",
      4: "Campus"
    }

    for key, value in student_menu_options.items():
      print(f'{key}. {value}')

      user_input = int(input("Enter the student details: "))
      return user_input

# FUNCTION FOR DELETE STUDENT MENU
  
  def student_delete_menu():
    user_input  = input("Enter student ID to delete the record: ")
    print("*******************\nDELETE STUDENT MENU\n*******************")
    return user_input
