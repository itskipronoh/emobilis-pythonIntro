
class Sent:
    first_name = "Felix"
    second_name = "Smith"
    age = 25
    student_id = 12345


class Person:
    def __init__(self, name, gender,occupation,age,martial_status):
        self.name = name
        self.gender = gender
        self.occupation = occupation
        self.age = age
        self.martial_status = martial_status

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")



class Vehicle:
    def __init__(self, vehicle_type, brand, model,color):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self):
        print(f"Type: {self.vehicle_type}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")