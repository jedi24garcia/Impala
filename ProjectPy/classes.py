#!/usr/bin/env python3

#CLASSES


import random
# from faker import Faker
import mimesis


class Student:
  def __init__(self, firstname, lastname, email, campus):
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
    self.firstname.generate()
    self.lastname.generate()
    self.email.generate()
    self.campus.generate()

  def firstname_generate(self):
    self.firstname = mimesis.first_name()

  def lastname_generator(self):
    self.lastname = mimesis.last_name()

  def email_generate(self):
    self.email = self.firstname + '.' + self.lastname + '@whitecliffe.ac.nz'

  def campus_generate(self):
    campuses = ["Auckland, Wellington, Christchurch"]
    self.campus = random.choices(campuses)

  def __str__(self):
    return "{} {} {} {}".format(
      self.firstname,
      self.lastname,
      self.email,
      self.campus,
    )
