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




