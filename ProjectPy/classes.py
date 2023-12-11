#!/usr/bin/env python3

import random
from faker import Faker

# Students

class Student:
    def __init__(self, id="", firstname="", lastname="", email="", campus=""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.campus = campus
        self.id = id


# Teachers

class Teacher:
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.qualification = ''
        self.age = 0
        self.campus = ''
        self.email = ''
        self.id = ''

    def input_teacher_details(self):
        print('Enter the following information for the new teacher:')
        self.firstname = input('First name: ')
        self.lastname = input('Last name: ')
        self.qualification = input('Qualification (one of PhD, Master, Bachelor: ')
        self.age = int(input('Age: '))
        self.campus = input("Campus (one of Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")
        self.email_generate()
        self.id_generate()

    def generate_data(self):
        self.firstname_generate()
        self.lastname_generate()
        self.qualification_generate()
        self.age_generate()
        self.campus_generate()
        self.email_generate()
        self.id_generate()

    def firstname_generate(self):
        # Initialize Faker to generate real names
        fake = Faker()
        self.firstname = fake.first_name()

    def lastname_generate(self):
        # Initialize Faker to generate real names
        fake = Faker()
        self.lastname = fake.last_name()

    def qualification_generate(self):
        # Define the ranges and their corresponding probabilities
        qualifications = ['PhD', 'Master', 'Bachelor']
        qual_probabilities = [0.2, 0.6, 0.2]

        # Calculate the weights based on the probabilities
        qual_weights = [prob / sum(qual_probabilities) for prob in qual_probabilities]
        self.campus = random.choices(qualifications, weights=qual_weights)[0]

    def age_generate(self):
        # Define the ranges and their corresponding probabilities
        age_ranges = [(20, 40), (40, 60), (60, 71)]
        age_probabilities = [0.3, 0.6, 0.1]

        # Calculate the weights based on the probabilities
        age_weights = [prob / sum(age_probabilities) for prob in age_probabilities]

        # Generate a random number based on the specified probability distribution
        random_range = random.choices(age_ranges, weights=age_weights)[0]
        self.age = random.randint(*random_range)

    def campus_generate(self):
        # Define the ranges and their corresponding probabilities
        campuses = ['Auckland', 'Hamilton', 'Wellington', 'Christchurch', 'Dunedin']
        campus_probabilities = [0.3, 0.2, 0.2, 0.2, 0.1]

        # Calculate the weights based on the probabilities
        campus_weights = [prob / sum(campus_probabilities) for prob in campus_probabilities]
        self.campus = random.choices(campuses, weights=campus_weights)[0]

    def email_generate(self):
        self.email = self.firstname + '.' + self.lastname + '@lecturer.whitecliffe.ac.nz'

    def id_generate(self):
        self.id = self.firstname[:3] + self.lastname[:3] + '_WHITECLIFFE'

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.qualification} {self.age} {self.email} {self.campus} {self.id}'


# class Teacher:
#     def __init__(self, firstname="", lastname="", qualification="", campus="", email="", id=""):
#         self.firstname =  firstname
#         self.lastname = lastname
#         self.qualification = qualification
#         self.campus = campus
#         self.email = email
#         self.id = id
    
#     def teacher_add_info(self):
#         print("\n*******************\nTEACHER ADD MENU\n*******************")
#         print("Enter the teachers details")
#         self.firstname = input("First Name: ")
#         self.lastname = input("Last Name: ")
#         self.qualification = input("Qualification (one of PhD, Master, Bachelor: ")
#         self.campus = input("Campus (Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")
#         # self.generate_email()
#         # self.generate_id()

#     def teacher_delete_info(teacher_db):
#         print("\n*******************\nDELETE TEACHER MENU\n*******************")
#         student_id = input("Enter teacher ID to delete the record: ")

#         teacher_db.delete_student(student_id)

#         print(f"**** Student with ID ({student_id}) is deleted from the system.")

        
#     def generate_teachers_data(self):
#         self.firstname_generate_data()
#         self.lastname_generate_data()
#         # self.qualification_generate_data()
#         # self.campus_generate_data()
#         # self.email_generate_data()
#         # self.id_generate_data()

#     def firstname_generate_data(self):
#         fake = Faker()
#         self.firstmame = fake.first_name()
        
#     def lastname_generate_data(self):
#         fake = Faker()
#         self.lastname = fake.first_name()
        

    