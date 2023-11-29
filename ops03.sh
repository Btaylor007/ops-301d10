#!/bin/bash
#11/29/2023
#ops challenge 03
# user for input directory path
read -p "Enter directory path: " dir_path

# user input permissions number
read -p "Enter permissions number: " permissions_num

cd "$dir_path"

# Change all files inside 
chmod -R "$permissions_num" *
#print directory list
ls -l
