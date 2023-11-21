#!/usr/bin/env python3

#UTILITY

import pandas as pd
import os, random

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
      students = self.read_student_data_file(filename)
  
  def generate_student_data_file():
    students = []
    for i in range(file_size):
      student = Student()
      student.generate_date()
      students.append(student)
    
    df = pd.DataFrame([s.__dict__ for s in students])
    
    df.to_csv(file_name, index=False)

    return student

class Menu():
  def main_menu(self):
    print("1. ADD NEW STUDENT")
    print("2. DELETE STUDENT")
    print("3. SHOW STUDENTS")
    print("4. SEARCH STUDENT")
    print("Type EXIT to quit your application")
    select = int(input("Enter your choice"))
    return select
