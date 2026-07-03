# Program: Personal Profile Generator

"""
learned:

 Variables and rules

 Basic types (str, int, float, bool, None)

 Arithmetic operators

 String operations (concat, index, slice, len)

 Type conversion

 User input

 f-strings
"""

"""
Write a program that:

Asks the user for:

    First name

    Last name

    Birth year

    Height in meters (can be decimal)

    Favorite color

Processes the data to display:

    Full name (first + last)

    Age (calculate from birth year - assume current year is 2026)

    Height in centimeters (multiply by 100 - store as integer)

    Initials (first letter of first name + first letter of last name)

    A secret code: reverse their full name and print it

    A fun fact: repeat their favorite color 5 times with spaces between
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("In which year you born? "))
height = input("What's your height in meter? ")
fav_color = input("Enter you favorite color: ")
current_year = 2026

full_name= f"{first_name} {last_name}"
age = current_year - birth_year
secret = full_name[::-1].lower()

print(f"Full name: {full_name}")
print(f"age: {age}")
print(f"Height in cm: {float(height)*100}")
print(f"Initials: {first_name[0]} {last_name[0]}")
print(f"secret: {secret}")
print(f"Favorite color 5 times: {(fav_color + ' ') * 5}")