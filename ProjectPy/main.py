#!/usr/bin/env python3

from classes import Student, Teacher
from utilities import student_database


def main():
    
    while True:
        print("\n**** Welcome TO WHITECLIFFE College of Information Technology ***")
        print("******************** STUDENT PORTAL *************************")
        print("CSV file 'student_data.csv' successfully loaded")
        print("\n1. Student")
        print("2. Teacher")
        print("3. Course")
        print("4. Exit Program")

        choice = input("Please select your choice: ").lower()

        if choice == "4":
            break
        elif choice == "1":
            second_menu()
        elif choice == "2":
            third_menu()
        elif choice == "3":
            second_menu()

def second_menu():

    while True:
        print("\nMAIN MENU")
        print("1. ADD NEW STUDENT")
        print("2. DELETE STUDENT")
        print("3. SHOW STUDENTS")
        print("4. SEARCH STUDENT")
        print("Type EXIT to quit this menu")

        choice = input("Enter your choice: ").lower()

        if choice == "exit":
            break
        elif choice == "1":
            add_new_student_menu(student_db)
        elif choice == "2":
            delete_student_menu(student_db)
        elif choice == "3":
            show_students_menu(student_db)
        elif choice == "4":
            search_student_menu(student_db)
        else:
            print("Invalid choice. Please try again.")

def third_menu():
    
    while True:
        print("\nMAIN MENU")
        print("1. ADD NEW TEACHER")
        print("2. DELETE TEACHER")
        print("3. SHOW TEACHER LIST")
        print("4. SEARCH FOR TEACHER")
        print("Type EXIT to quit this menu")
        
        choice = input("Enter your choice: ").lower()

        if choice == "exit":
            break
        elif choice == "1":
            teacher = Teacher()
            teacher.teacher_add_info()

def add_new_student_menu(student_db):
    print("\n*******************\nSTUDENT ADD MENU\n*******************")
    print("Enter the student details")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    email = input("Enter Email Address: ")
    campus = input("Campus (Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")

    new_student = Student(firstname, lastname, email, campus)
    student_db.add_new_student(new_student)

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
    student_db = student_database()
    student_db.txt_to_csv()
    main()
