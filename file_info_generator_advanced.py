"""
Create a script to that generates a list of dictionaries about files in the working directory. Then print the list.

Push your code to GitHub and include the link in your write up.

ADVANCED
Modify the script into a function such that any path can be passed as a parameter. This parameter should be optional and should default to working directory when the variable is not passed. The function should then create the list of dictionaries about files from that path. The function should also return information on files nested in folders (recursive).

‌
"""
import os

# Define a function that retrieves file information in a directory.
def get_directory_files_info(directory_path='.'):
    # If a specific directory path is not provided, default to the current working directory.
    current_dir = os.getcwd() if directory_path == '.' else directory_path
    
    # Get the list of file names in the specified directory.
    file_names = os.listdir(current_dir)
    
    # Create an empty list to store file information as dictionaries.
    files_info = []

    # Iterate through the file names in the directory.
    for filename in file_names:
        # Construct the full file path by joining the directory path and file name.
        file_path = os.path.join(current_dir, filename)
        
        # Check if the path points to a file or symbolic link.
        if os.path.isfile(file_path) or os.path.islink(file_path):
            # Create a dictionary containing the file path and its size.
            file_info = {
                "file_path": file_path,
                "file_size": os.path.getsize(file_path)
            }
            # Append the file information dictionary to the list.
            files_info.append(file_info)

    # Return the list of file information.
    return files_info

# Call the function without providing a directory path to use the default (current working directory).
file_info_list = get_directory_files_info()

# Print the list of dictionaries containing file information.
for file_info in file_info_list:
    print(file_info)
