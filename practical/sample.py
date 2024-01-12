#!/usr/bin/env python3

import csv

# CLASS

class Student:
    def __init__(self, firstname="", lastname="", email="", campus=""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.campus = campus
       
class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

    def show_students(self, order_by):
        # Implementation of sorting logic based on order_by parameter
        # Use Python's built-in sorting functions
        sorted_students = sorted(self.students, key=lambda x: getattr(x, order_by))
        for student in sorted_students:
            print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")

    def search_student(self, search_by, value):
        # Implementation of searching logic based on search_by parameter
        # Use Python's built-in filtering functions
        result_students = [s for s in self.students if getattr(s, search_by) == value]
        for student in result_students:
            print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")

    def txt_to_csv(self):
        with open('student_data.txt', mode="r", newline="") as txt_file:
          lines = txt_file.readlines()

        with open('student_data.csv', mode="w", newline="") as csv_file: 
          fieldnames = ['First Name', 'Last Name', 'Email', 'Campus']
          writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t') 

          writer.writeheader()

          for line in lines:
              data = line.strip().split('\t')
              if len(data) >= 4:
                writer.writerow({
                  # 'ID': student.id,
                    'First Name': data[0],
                    'Last Name': data[1],
                    'Email': data[2],
                    'Campus': data[3],
                })

def main():

    while True:
        print("\n**** Welcome TO WHITECLIFFE College of Information Technology ***")
        print("******************** STUDENT PORTAL *************************")
        print("CSV file 'student_data.csv' successfully loaded")
        print("\nMAIN MENU")
        print("1. ADD NEW STUDENT")
        print("2. DELETE STUDENT")
        print("3. SHOW STUDENTS")
        print("4. SEARCH STUDENT")
        print("Type EXIT to quit the application")

        choice = input("Enter your choice: ").lower()

        if choice == 'exit':
            break
        elif choice == '1':
            add_student_menu(student_db)
        elif choice == '2':
            delete_student_menu(student_db)
        elif choice == '3':
            show_students_menu(student_db)
        elif choice == '4':
            search_student_menu(student_db)
        else:
            print("Invalid choice. Please try again.")

def add_student_menu(student_db):
    print("\n*******************\nSTUDENT ADD MENU\n*******************")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    email = input("Enter Email Address: ")
    campus = input("Enter Campus: ")

    new_student = Student(firstname, lastname, email, campus)
    student_db.add_student(new_student)

    print("\n*** Record Successfully added. ***")

def delete_student_menu(student_db):
    print("\n*******************\nDELETE STUDENT MENU\n*******************")
    student_id = input("Enter student ID to delete the record: ")

    student_db.delete_student(student_id)

    print(f"**** Student with ID ({student_id}) is deleted from the system.")

def show_students_menu(student_db):
    print("\n*******************\nSTUDENTS SHOW MENU\n*******************")
    print("1. SHOW ALL STUDENTS BY ID")
    print("2. SHOW ALL STUDENTS BY FIRST NAME (ASCENDING ORDER)")
    print("3. SHOW ALL STUDENTS BY LAST NAME (ASCENDING ORDER)")
    print("4. SHOW ALL STUDENTS BY CAMPUS (ASCENDING ORDER)")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_db.show_students('id')
    elif choice == '2':
        student_db.show_students('firstname')
    elif choice == '3':
        student_db.show_students('lastname')
    elif choice == '4':
        student_db.show_students('campus')
    else:
        print("Invalid choice. Please try again.")

def search_student_menu(student_db):
    print("\n*******************\nSTUDENT SEARCH MENU\n*******************")
    print("1. SEARCH STUDENT BY ID")
    print("2. SEARCH STUDENT BY FIRST NAME")
    print("3. SEARCH STUDENT BY LAST NAME")

    choice = input("Enter your choice: ")

    if choice == '1':
        search_by = 'id'
    elif choice == '2':
        search_by = 'firstname'
    elif choice == '3':
        search_by = 'lastname'
    else:
        print("Invalid choice. Please try again.")
        return

    search_value = input(f"Enter the {search_by} to search: ")
    student_db.search_student(search_by, search_value)

if __name__ == "__main__":
    student_db = StudentDatabase()
    student_db.txt_to_csv()
    main()
