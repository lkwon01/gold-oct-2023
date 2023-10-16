'''
This week you will again be documenting your projects in Medium from this point forward now that your projects contain more substance outside of basic Python.

‌

Scenario: Your company needs to learn about the files located on various machines. You have been asked to build a script that extracts information such as the name and size about the files in the current working directory and stores it in a list of dictionaries.



Create a script to that generates a list of dictionaries about files in the working directory. Then print the list.

Push your code to GitHub and include the link in your write up.

‌‌

'''
# Import the os module for file and directory operations.
import os

# Get the current working directory.
current_dir = os.getcwd()

# List all files and directories in the current working directory.
files = os.listdir(current_dir)

# Create an empty list to store file information as dictionaries.
files_list = []

# Iterate through the files and directories in the current directory.
for file in files:
    # Construct the full file path by joining the current directory and the file name.
    file_path = os.path.join(current_dir, file)
    
    # Check if the path points to a file (not a directory).
    if os.path.isfile(file_path):
        # Create a dictionary containing the file name and its size.
        file_info = {
            "file_name": file,
            "file_size": os.path.getsize(file_path)
        }
        
        # Append the file information dictionary to the list.
        files_list.append(file_info)

# Print the list of dictionaries containing file information.
print(files_list)


