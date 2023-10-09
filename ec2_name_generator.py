
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
