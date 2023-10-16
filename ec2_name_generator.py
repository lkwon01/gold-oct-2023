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
#https://peps.python.org/pep-0008/
#https://www.w3schools.com/python/module_random.asp
#https://www.w3schools.com/python/ref_random_choice.asp
#https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=python
#https://www.udemy.com/course/python-pcep/
#https://aws.plainenglish.io/how-to-use-aws-cloud9-with-github-3136692fa44d

import random
import string
import sys

# List of allowed department names
allowed_departments = ["Marketing", "Accounting", "Finops"]

# Function to get a valid instance number from the user
def get_valid_instance_number():
    while True:
        try:
            # Attempt to convert user input to an integer
            instance_number = int(input('How many EC2 instances do you want to name? '))
            if instance_number > 0:
                print('Thank you! Let\'s generate', instance_number, 'instance names')
                return instance_number
            else:
                print("Please enter a positive integer for the number of instances.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

# Function to generate EC2 instance names
def generate_ec2_names():
    instance_number = get_valid_instance_number()
    
    # Prompt the user for department name until a valid one is entered
    while True:
        dept_name = input('Please enter your department name (Marketing, Accounting, or FinOps): ')
        dept_name = dept_name.capitalize()  # Capitalize the input
        
        # Check if the department is allowed
        if dept_name in allowed_departments:
            break
        else:
            print("This department is not allowed. Please enter a valid department name.")
    
    ec2_names = []

    # Generate EC2 names based on the department and random characters/numbers
    for _ in range(instance_number):
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        random_numbers = ''.join(random.choices(string.digits, k=3))
        ec2_name = f"{dept_name}-{random_chars}-{random_numbers}"
        ec2_names.append(ec2_name)

    return ec2_names

# Generate EC2 instance names and print them
generated_names = generate_ec2_names()
for name in generated_names:
    print(name)
