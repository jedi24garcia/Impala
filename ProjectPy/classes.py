#!/usr/bin/env python3

#CLASSES


import random
from faker import Faker
# import mimesis


class Student:
  faker = Faker()

  def __init__(self, firstname="", lastname="", email="", campus=""): 
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.campus = campus

  def student_info(self):
    print("Enter the student details")
    self.firstname = input("First Name: ")
    self.lastname = input("Last Name: ")
    self.email = input("Email Address: ")
    self.campus = input("Campus: ")

  def generate_info(self):
    self.firstname_generate()
    self.lastname_generate()
    self.email_generate()
    self.campus_generate()

  def firstname_generate(self):
    # faker = Faker()
    self.firstname = self.faker.first_name()

  def lastname_generate(self):
    # faker = Faker
    self.lastname = self.faker.last_name()

  def email_generate(self):
    self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@whitecliffe.ac.nz'

  def campus_generate(self):
    campuses = ["Auckland, Wellington, Christchurch"]
    self.campus = random.choice(campuses)

  def __str__(self):
    return "{} {} {} {}".format(
      self.firstname,
      self.lastname,
      self.email,
      self.campus,
    )
