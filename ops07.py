#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

user_input_path = input("Enter a directory path: ")

# Declaration of functions

def generate_directory_info(path):
    for (root, directories, files) in os.walk(path):
        print(f"\n== Root directory: {root} ==")
        print(f"Directories: {directories}")
        print(f"Files: {files}")


# Get user input
user_path = input("Enter a directory path: ")

# Generate directory information
generate_directory_info(user_path)
