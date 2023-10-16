"""
John has a hard time keeping his budget. Write a program to help him analyse his spendings. You are given a list with John's spendings for each month. Go through the list, and count the number of times...

a. the spendings were low (< 1000.0)
b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
c. the spendings were high (> 2500.0)

Then, print the following to the output:

Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.
"""
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

num_low = 0
num_normal = 0
num_high =0

for spending in spendings:
    if spending < 1000.0:
        num_low += 1
    
    elif 1000 <= spending <= 2500.0:
        num_normal += 1
    
    else:
        num_high += 1
        
        
print ('Numbers of months with low spendings:', num_low, ', normal spendings:',num_normal, ', high spendings:',num_high, '.')
        
    
    
        
    
        