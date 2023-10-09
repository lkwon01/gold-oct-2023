"""
Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
2. Allow the user to input the name of their department that is used in the unique name.
3. Generate random characters and numbers that will be included in the unique name.
4. Push your code to GitHub and include the link in your LinkedIn write up.

ADVANCED
The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.

COMPLEX
Turn the above into a Function and execute the Function to verify it works.
"""
#<Resources>
#https://docs.python.org/3/library/random.html
#https://www.w3schools.com/python/module_random.asp
#https://peps.python.org/pep-0008/

import random
import string

print('Welcome to the World\' best password generator!!!')
# Define the characters you want in your password
letters = string.ascii_letters  # includes both uppercase and lowercase letters
digits = string.digits  # includes numbers
special_characters = string.punctuation  # includes special characters like !@#$%^&*()

# Combine all the characters into one string
all_characters = letters + digits + special_characters

# Ask the user for the desired length of the password
while True:
    try:
        password_length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

# Generate the password
password = ''.join(random.choice(all_characters) for _ in range(password_length))

# Print the generated password
print("Generated Password:", password)




