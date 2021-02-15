# instructions
# Here is a python code that generate a list of 20000 random numbers, called list_of_numbers.
# -> Extend this code to guess how many couples of numbers in list_of_numbers sum to target_number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(2000)]
target_number   = 3728   


print(list_of_numbers)
count = 0
for i in range(len(list_of_numbers)):
    for j in range(len(list_of_numbers)):
        if list_of_numbers[j]+list_of_numbers[i] == target_number:
            # print(f"{i} + {j} = {target_number} ")
            count += 1
            if j == i:
                count += 1
            
        


print(f"they are {count/2} couples of number equal to {target_number}")
