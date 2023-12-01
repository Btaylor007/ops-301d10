#!/bin/bash

#functions
functions hello_world() { echo "Hello, World!"; }
functions ping_self() { ping localhost; }
functions ip_info() { ip addr show; }

# Main menu 
if true; do
  # Display menu
  clear
  echo "Bash Menu System"
  echo "1. Hello World"
  echo "2. Ping Self"
  echo "3. IP Info"
  echo "4. Exit"

  
  echo "Enter choice: "
  read choice 
fi
  # user input actions 
  case $choice in
    1) hello_world ;;
    2) ping_self ;;
    3) ip_info ;;
    4) exit 0 ;;
    *) echo "Invalid choice. Please enter a number between 1 and 4." ;;
  esac

  # Press Enter to continue
  read -n 1 -r -p "Press Enter to continue..."
  #https://linuxhint.com/bash_conditional_statement/ website cited 
done
