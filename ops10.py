breanna taylor
12/10/2023
opschallenge10

with open("data.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

with open("data.txt", "r") as f:
    print(f.readline())

import os
os.remove("data.txt")
