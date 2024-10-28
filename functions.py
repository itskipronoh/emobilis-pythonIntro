
def myfunction():
    print("Hello Andrew")
    print("This is a function")
    print("Goodbye Andrew")

myfunction()
myfunction()
myfunction()

def my_function(first_name, last_name , age):
    print(f"Hello {first_name} {last_name} you are {age} years old")

my_function("Andrew", "Yotui", 25)
my_function("Jane", "wambui", 30)
my_function("felix", "korir", 40)

def promote(first_name, last_name, age,):
    if age >= 18:
        print(f"Hello {first_name} {last_name} you are {age} years old and you are promoted to the next class")
    elif age >= 30:
        print(f"Hello {first_name} {last_name} you are {age} years old and you are promoted to the ranking class")
    elif age >= 40:
        print(f"Hello {first_name} {last_name} you are {age} years old and you are retired")
    else:
        print(f"Hello {first_name} {last_name}Congratulations")

def greet(name):
    if name == "Alice" or name == "Bob":
        return f"Hello, {name}! Welcome back!"
    else:
        return "Hello! Nice to meet you!"


print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))


def find_max(num1, num2, num3):
    return max(num1, num2, num3)


num1 = 5
num2 = 12
num3 = 9
print("The maximum number is:", find_max(num1, num2, num3))


def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_numbers([1, 2, 3, 4, 5]))


def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(5, 10)







def add_numbers(num1, num2):

    summation = num1 + num2

    print(f"The sum of {num1} and {num2} is {summation}")


add_numbers(5, 10)




