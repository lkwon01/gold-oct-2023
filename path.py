"""
Your module description
"""
import os

directory_path = os.getcwd()
files = os.listdir()

files_info = []

# Iterate through each item (file or directory) in the current working directory
for item in files:
    item_path = os.path.join(directory_path, item)  # Create the full path for the item
    is_directory = os.path.isdir(item_path)  # Check if the item is a directory

    # Append to the files_info list based on whether it's a file or a directory
    if is_directory:
        files_info.append(f"Directory: {item_path}")
    else:
        files_info.append(f"File: {item_path}")

# Print the resulting list of files and directories with their types
for item_info in files_info:
    print(item_info)
