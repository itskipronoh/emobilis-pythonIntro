
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


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount.")

    def apply_bank_fees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Bank fees applied: {fee}")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance:.2f}")


