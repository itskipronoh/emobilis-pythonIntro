
name = "Kiprono"
age = 30
occupation = "Developer"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Occupation: {occupation}")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You have a normal weight.")
elif bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")