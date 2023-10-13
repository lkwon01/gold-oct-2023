"""
Your module description
"""
import random
import string

num_instance =int(input('how many: '))

# print('hello')
# char = string.ascii_letters
# print(char)
# char = string.digits
# print(char)
# char = string.ascii_letters + string.digits
# print(char)
# char = random.choices(string.ascii_letters, k=3)
# print(char)
# char = ''.join(random.choices(string.ascii_letters, k=3))
# print(char)
# num = ''.join(random.choices(string.digits, k=3))
# print(num)
# name = char + num
# print(name)

for i in range(num_instance):
    
    char = ''.join(random.choices(string.ascii_letters, k=3))
   
    num = ''.join(random.choices(string.digits, k=3))
 
    name = char + num
    print(name)