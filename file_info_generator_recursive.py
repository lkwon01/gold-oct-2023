"""
This week you will again be documenting your projects in Medium from this point forward now that your projects contain more substance outside of basic Python.

Scenario: Your company needs to learn about the files located on various machines. You have been asked to build a script that extracts information such as the name and size about the files in the current working directory and stores it in a list of dictionaries.

FOUNDATIONAL


Create a script to that generates a list of dictionaries about files in the working directory. Then print the list.

Push your code to GitHub and include the link in your write up.


ADVANCED
Modify the script into a function such that any path can be passed as a parameter. This parameter should be optional and should default to working directory when the variable is not passed. The function should then create the list of dictionaries about files from that path. The function should also return information on files nested in folders (recursive).

COMPLEX (Very Tricky)

Modify the function to display recursive file information as dictionary of dictionaries.
"""
# Import the os module for file and directory operations.
import os

# Welcome message to the user
print('Welcome! Please enter the directory name. We will extract information such as the name and size about the files in the directory for you.')


def get_directory_files_info(directory_path='.', recursive=True):
    files_info = []
   
    # Use os.walk to recursively iterate over all files/directories in the specified directory.
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Join the directory path and filename to get the full file path.
            file_path = os.path.join(root, file)
            
            # Create a dictionary for each file with its size.
            file_info = {
                "file_path": file_path,
                "file_size": os.path.getsize(file_path)
            }
            # Append the file information dictionary to the list.
            files_info.append(file_info)
    
    return files_info

def dir_input():
    # Prompt the user to input the directory path
    dir_input = input("Enter the directory name: ")
    if not dir_input:
        dir_input = os.getcwd()  # Use the current directory if no input is provided
    else:
        dir_input = os.path.abspath(dir_input)  # Get the absolute path of the user-provided directory
        
    result = get_directory_files_info(dir_input)
    
    # Display the file information to the user
    for r in result:
        print(r)

# Call the dir_input function to start the process
dir_input()
