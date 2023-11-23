#!/usr/bin/env python3

#UTILITY

import pandas as pd
import os, random
from classes import Student

class utility():
  def file_exists(self, file_name):
    if os.path.isfile(file_name):
      return True
    else:
      return False

  def student_data_file(self, file_name, file_size):
    if not self.file_exists(file_name):
      print("File does not exist. I will generate a new one.")
      students = self.generate_student_data_file(file_name, file_size)
      print("File generated successfully")
    else:
      print("File exists. I will read from it instead.")
      students = self.read_student_data_file(file_name)
      # students = self.student_data_file(file_name, file_size)
  
    return students
    
  def generate_student_data_file(self, file_name, file_size):
    students = []
    for i in range(file_size):
      student = Student()
      # student.firstname_generate()
      # student.lastname_generate()
      # student.email_generate()
      # student.campus()
      student.generate_info()
      students.append(student)
    
    df = pd.DataFrame([s.__dict__ for s in students])
    
    df.to_csv(file_name, index=False)

    return students
  
  def read_student_data_file(self,file_name):
      # Read the CSV file into a DataFrame
      df = pd.read_csv(file_name)

      # Convert the DataFrame into a list of Student objects
      students = []
      for i in range(len(df)):
          student = Student()
          student.__dict__ = df.iloc[i].to_dict()
          students.append(student)

      return students

  def save_student_data_file(self,file_name,students):
      # Convert the list of Student objects into a DataFrame
      df = pd.DataFrame([s.__dict__ for s in students])

      # Write the DataFrame into a CSV file
      df.to_csv(file_name, index=False)

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
