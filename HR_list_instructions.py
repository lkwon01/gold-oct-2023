'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''




if __name__ == '__main__':
    N = int(input('Enter number:'))  # Read an integer N from the user
    
    answer_list = []  # Initialize an empty list called 'answer_list' to store values
    
    for i in range(N):
        instruction = input('Enter instruction: ')  # Read a user instruction as a string
        tokens = instruction.split(" ")  # Split the instruction into a list of tokens
        
        if tokens[0] == "insert":
            # If the instruction is 'insert', insert an element at the specified index
            answer_list.insert(int(tokens[1]), int(tokens[2]))
            
        elif tokens[0] == "print":
            # If the instruction is 'print', print the contents of 'answer_list'
            print(answer_list)
        elif tokens[0] == "remove":
            # If the instruction is 'remove', remove the first occurrence of the specified value
            answer_list.remove(int(tokens[1]))
        elif tokens[0] == "append":
            # If the instruction is 'append', add an element to the end of 'answer_list'
            answer_list.append(int(tokens[1]))
        elif tokens[0] == "sort":
            # If the instruction is 'sort', sort 'answer_list' in ascending order
            answer_list.sort()
        elif tokens[0] == "pop":
            # If the instruction is 'pop', remove and return the last element of 'answer_list'
            answer_list.pop()
        elif tokens[0] == "reverse":
            # If the instruction is 'reverse', reverse the order of elements in 'answer_list'
            answer_list.reverse()
