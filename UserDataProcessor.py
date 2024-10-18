# 2. User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for and checks the 
# length of the user's first name and last name. Both should be at least 2 characters 
# long. If not, print an error message.

# NOTE: Ensure that all code in your file is ready to run. 
# This means that if someone opens your file and clicks the run 
# button at the top, all code executes as intended. For example, 
# if there are if statements, print statements, or for loops, 
# they should function correctly and display output in the console as 
# expected. If you have a function, make sure the function is called and runs.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

first_name = input("Please enter your first name (must be at least two characters): \n")
last_name = input("Please enter your last name (must be at least two characters): \n")

if len(first_name) < 2:
    print("Sorry that was invalid. Please enter a first_name of two characters or more.")
elif len(last_name) < 2:
    print("Sorry that was invalid. Please enter a last_name of two characters or more.")
else:
    print(f"Your first name is {len(first_name)} characters long and your last name is {len(last_name)} characters long.")