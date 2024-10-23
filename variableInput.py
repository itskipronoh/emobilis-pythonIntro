
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


withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
if withdrawal_amount > 10000:
    discount_rate = 0.15
elif withdrawal_amount > 5000:
   discount_rate = 0.10
elif withdrawal_amount > 2000:
    discount_rate = 0.05
else:
    discount_rate = 0.00

discount_amount = withdrawal_amount * discount_rate

total_amount = withdrawal_amount - discount_amount

print(f"Discount Awarded: {discount_rate:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Total Amount: {total_amount:.2f}")
print(f"Thank you for banking with us.")


