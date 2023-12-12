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
    def __init__(self, firstname="", lastname="", qualification="", age="", campus="", email="", id=""):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.campus = campus
        self.qualification = qualification
        self.email = email
        self.id = id

    def teacher_add_info(self):
        print("\n*******************\nTEACHER ADD MENU\n*******************")
        print("\nEnter the following information for the new teacher: ")
        self.firstname = input('First name: ')
        self.lastname = input('Last name: ')
        self.age = int(input('Age: '))
        self.campus = input("Campus (one of Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")
        self.qualification = input('Qualification (PhD, Master, Bachelor, Diploma): ')
        print(f"\nNew teacher ({self.firstname}) ({self.lastname}) ({self.age}) ({self.campus}) ({self.qualification}) has been added to the system.")
        self.email_generate()
        self.id_generate()

    def teacher_delete_info(self):
        print("\n*******************\nDELETE TEACHER MENU\n*******************")
        teacher_id = input("\nEnter teacher ID to delete the record: ")
        print(f"\n**** Teacher with ID ({teacher_id}) is deleted from the system.")


    def show_search_data(self):
        print("1. First Name")
        print("2. Last Name")
        print("3. Age")
        print("4. Campus")
        print("5. Qualification")
        print("6. Email")
        print("7. ID")
        choice = input("Please choose a number: ")
        return choice

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
        return "{} {} {} {} {} {} {}".format(
            self.firstname,
            self.lastname,
            self.qualification,
            self.age,
            self.email,
            self.campus,
            self.id,
        )

    # def __str__(self):
    #     return f'{self.firstname} {self.lastname} {self.qualification} {self.age} {self.email} {self.campus} {self.id}'

        

    