
from main import Student
from main import Person
from main import Vehicle

student1 = Student("Alice", 25, 12345)
student1.display_info()
student2 = Student("Bob", 30, 12346)
student2.display_info()

person1 = Person("Alice", "Male", "Engineer", 25, "Single")
print(person1.name)

vehicle1 = Vehicle("Car", "Toyota", "Corolla", "Red")
vehicle2 = Vehicle("Motorbikes", "Yamaha", "MT-07", "Blue")
vehicle3 = Vehicle("Truck", "Ford", "F-150", "Black")
vehicle4 = Vehicle("Pickup", "Isuzu", "double-cab", "Green")
vehicle5 = Vehicle("Van", "Nissan", "NV200", "White")
vehicle6 = Vehicle("Bus", "Isuzu", "NQR", "Yellow")


vehicle1.display_info()
vehicle2.display_info()
vehicle3.display_info()
vehicle4.display_info()
vehicle5.display_info()
vehicle6.display_info()


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

    def display_dimensions(self):
        print(f"Width: {self.width}")
        print(f"Length: {self.length}")

# Example usage
rectangle = Rectangle(5, 10)
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Area: {rectangle.area()}")
rectangle.display_dimensions()