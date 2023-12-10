class Student:
    def __init__(self, first_name, last_name, email, campus):
        self.id = self.generate_id(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.campus = campus

    def generate_id(self, first_name, last_name):
        # Implementation of ID generation logic
        return f"{first_name[:3]}{last_name[:3]}{str(2023)[-2:]}"

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
            print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Email: {student.email}, Campus: {student.campus}")

    def search_student(self, search_by, value):
        # Implementation of searching logic based on search_by parameter
        # Use Python's built-in filtering functions
        result_students = [s for s in self.students if getattr(s, search_by) == value]
        for student in result_students:
            print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Email: {student.email}, Campus: {student.campus}")

def main():
    student_db = StudentDatabase()

    while True:
        print("\n**** Welcome TO WHITECLIFFE College of Information Technology ***")
        print("******************** STUDENT PORTAL *************************")
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
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email Address: ")
    campus = input("Enter Campus: ")

    new_student = Student(first_name, last_name, email, campus)
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
        student_db.show_students('first_name')
    elif choice == '3':
        student_db.show_students('last_name')
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
        search_by = 'first_name'
    elif choice == '3':
        search_by = 'last_name'
    else:
        print("Invalid choice. Please try again.")
        return

    search_value = input(f"Enter the {search_by} to search: ")
    student_db.search_student(search_by, search_value)

if __name__ == "__main__":
    main()
