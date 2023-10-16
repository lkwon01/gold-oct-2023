"""
Your module description


"""
def find_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

user_input = input('Enter a list of elements separated by spaces: ')
input_list = user_input.split()  # Split the input string into a list of elements

unique_elements = find_unique_elements(input_list)

print("Unique elements in the list:", unique_elements)


    
