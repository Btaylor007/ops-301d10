age = 20

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

number = 10

if number > 10:
    print("The number is greater than 10.")
elif number == 10:
    print("The number is equal to 10.")
else:
    print("The number is less than 10.")

a = 5
b = 10

# Check for equality
if a == b:
    print(f"a ({a}) is equal to b ({b})")
else:
    print(f"a ({a}) is not equal to b ({b})")

# Check for different conditions
conditions = [
    (a != b, "a is not equal to b"),
    (a < b, "a is less than b"),
    (a <= b, "a is less than or equal to b"),
    (a > b, "a is greater than b"),
    (a >= b, "a is greater than or equal to b"),
]

for condition, message in conditions:
    if condition:
        print(message)
        break
