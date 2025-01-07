#!/usr/bin/env python3
print("- Create a program thaat takes user input for their name and age then prints a greeting with their name and calculates the year they were born")

#Provide users input for name and age
name = input("Enter your name: ")


age = int(input("Enter your age: "))

# Calculate the year the user was born
current_year = 2025
birth_year = current_year - age

# Print a greeting with the user's name and the calculated birth year
print(f"Hey there, {name}! You were born in {birth_year}.")
