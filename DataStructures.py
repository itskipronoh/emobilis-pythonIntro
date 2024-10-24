
vehicles = {
    'car': 'Toyota',
    'motorcycle': 'Yamaha',
    'truck': 'Ford',
    'bus': 'Mercedes-Benz',
    'bicycle': 'Giant'
}


vehicle_to_check = 'Toyota'


if vehicle_to_check in vehicles.values():
    print(f"{vehicle_to_check} is present in the vehicle list.")
else:
    print(f"{vehicle_to_check} is not found in the vehicle list.")


vehicle_to_check = 'Honda'

if vehicle_to_check in vehicles.values():
    print(f"{vehicle_to_check} is present in the vehicle list.")
else:
    print(f"{vehicle_to_check} is not found in the vehicle list.")


ages = []

for i in range(4):
    age = int(input(f"Enter the age of user {i + 1}: "))
    ages.append(age)


all_above_18 = all(age > 18 for age in ages)
at_least_one_below_18 = any(age < 18 for age in ages)
all_same_age = all(age == ages[0] for age in ages)


print(f"Ages: {ages}")
print(f"All users are above 18: {all_above_18}")
print(f"At least one user is below 18: {at_least_one_below_18}")
print(f"All users have the same age: {all_same_age}")
















import random
random_dict = {f"key_{i}": random.randint(1, 100) for i in range(5)}
print("Random Dictionary:", random_dict)
key_to_check = "key_3"
if key_to_check in random_dict:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")



ages = []

for i in range(4):
    age = int(input(f"Enter the age of user {i + 1}: "))
    ages.append(age)


all_above_18 = all(age > 18 for age in ages)
at_least_one_below_18 = any(age < 18 for age in ages)
all_same_age = all(age == ages[0] for age in ages)


print(f"Ages: {ages}")
print(f"All users are above 18: {all_above_18}")
print(f"At least one user is below 18: {at_least_one_below_18}")
print(f"All users have the same age: {all_same_age}")




ages = [int(input(f"Enter age for user {i+1}: ")) for i in range(4)]

average_age = sum(ages) / len(ages)
max_age = max(ages)
min_age = min(ages)

print(f"Average Age: {average_age:.2f}")
print(f"Oldest Age: {max_age}")
print(f"Youngest Age: {min_age}")

if all(age >= 18 for age in ages):
    print("All users are adults.")
else:
    print("Not all users are adults.")
