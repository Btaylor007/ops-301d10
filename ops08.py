#list
fruits = ["apple", "banana", "cherry", "orange", "mango", "grapefruit", "kiwi", "melon", "pineapple", "strawberry"]

# Print the fourth of the list
print(fruits[3])  # output: orange

# Print the sixth through ten  of the list
print(fruits[5:])  # output: ['grapefruit', 'kiwi', 'melon', 'pineapple', 'strawberry']

# Change the value of the seven to "onion"
fruits[6] = "onion"

# Print the modified list
print(fruits)  # output: ['apple', 'banana', 'cherry', 'orange', 'mango', 'grapefruit', 'onion', 'melon', 'pineapple', 'strawberry']

# Print the sixth through tenth element using slicing
print("Elements 6 to 10:")
for fruit in fruits[5:]:
    print(f"\t- {fruit}")

# Print the updated list (optional)
print("\nUpdated list:")
for fruit in fruits:
    print(fruit)
