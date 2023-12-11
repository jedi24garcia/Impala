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
    def __init__(self, firstname="", lastname="", qualification="", campus="", email="", id=""):
        self.firstname =  firstname
        self.lastname = lastname
        self.qualification = qualification
        self.campus = campus
        self.email = email
        self.id = id
    
    def teacher_add_info(self):
        print("\n*******************\nTEACHER ADD MENU\n*******************")
        print("Enter the teachers details")
        self.firstname = input("First Name: ")
        self.lastname = input("Last Name: ")
        self.qualification = input("Qualification (one of PhD, Master, Bachelor: ")
        self.campus = input("Campus (Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")
        # self.generate_email()
        # self.generate_id()

        
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
        

    