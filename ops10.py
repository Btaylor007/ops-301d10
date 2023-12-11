# Create a new file
with open("data.txt", "w") as f:
    # Append three lines
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Open the file in read mode
with open("data.txt", "r") as f:
    # Read the first line
    first_line = f.readline()

# Print the first line to the screen
print(first_line)

# Delete the file
import os
os.remove("data.txt")

print("File deleted successfully!")
