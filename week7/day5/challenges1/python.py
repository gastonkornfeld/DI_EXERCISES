
import math

# Exercise 1
# Write a script that inserts an item at a defined index in a list.
list_1 = [num for num in range(0,100)]

def insert_item_in_a_list(list1, index, insert):
    new_list = []
    for i in range(index-1):
        new_list.append(list1[i])
    new_list.append(insert)
    for i in range(index, len(list1)):
        new_list.append(list1[i])
    
    return new_list



print(insert_item_in_a_list(list_1, 33, "chau"))


# Exercise 2
# Write a script that counts the number of spaces in a string.

def count_spaces(string):
    count_space = 0
    for letter in string:
        if letter == " ":
            count_space += 1
    return count_space

print(count_spaces("iadaosd ad uasdha d asdha sdhalsfha sfahsfoiash foashf iasf"))




# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def count_upper_and_lower(string):
    string_to_lower = string.lower()
    string_to_upper = string.upper()
    count_upper = 0
    count_lower = 0
    for i in range(len(string)):
        # if it is a space i just pass
        if string[i] == " ":
            continue
        # if the letter is uppercase
        elif string[i] == string_to_upper[i]:
            count_upper += 1
        elif string[i] == string_to_lower[i]:
            count_lower += 1
    return f"They are {count_lower} lower characters and {count_upper} upper characters in the string."



print(count_upper_and_lower("ajdbakdbakdhbask JHKJHKJb Ujkdbsa JB kJH "))



# Exercise 4
# Write a function to find the max of a list

def find_max_list(list_numbers):
    for i in range(len(list_numbers)-1):
        for i in range(len(list_numbers)-1): 
            if list_numbers[i] < list_numbers[i+1]:
                item_to_copy = list_numbers[i]
                list_numbers[i] = list_numbers[i+1]
                list_numbers[i+1] = item_to_copy
    return f"the max number of the list given is: {list_numbers[0]}"

print(find_max_list(list_1))



# Write a function that return factorial of a number


def factorial(number):
    factorial_result = number
    for i in range(number-1, 1, -1):
        factorial_result *= i
    return f"the factorial of {number} is: {factorial_result}"

print(factorial(7))





# Write a function to find the sum of an array without using the built in function:

#     >>>MySum([1,5,4,2])
#     >>>12

def sum_of_array(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number

    return f" the total is: {total}"


print(sum_of_array(list_1))





# Write a function that counts an element in a list (without using the count method):
def count_element_in_list(element, list_of_things):
    total_of_times = 0
    for elements in list_of_things:
        if element == elements:
            total_of_times += 1
    if total_of_times == 1:
        return f"the element {element} is only {total_of_times} time in the list given"
    return f"the element {element} is {total_of_times} times in the list given"


print(count_element_in_list(2, [2,2,2,2,4,4,3,3,2]))








# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>Norm([1,2,2])
#     >>>3
# ​


def norm(list_of_numbers):
    sum_of_sqaures = 0
    for number in list_of_numbers:
        sum_of_sqaures += number**2
    root_of_the_sum = math.sqrt(sum_of_sqaures)
    return f"the norm of the list is: {root_of_the_sum}"


print(norm([1,2,2]))




