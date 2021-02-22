
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







# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)


def is_monotonic(list_of_numbers):
    is_monotonic = True
    for i in range(len(list_of_numbers)- 2):
        if list_of_numbers[i] > list_of_numbers[i + 1] and list_of_numbers[1 + i] < list_of_numbers[i + 2]:
            return False
        if list_of_numbers[i] < list_of_numbers[i + 1] and list_of_numbers[1 + i] > list_of_numbers[i + 2]:
            return False

    return is_monotonic




print(is_monotonic([0, 1, 2, 3, 4, 5, 6]))
print(is_monotonic([0, 1, 2, 3, 4, 5, 4]))
print(is_monotonic([0, 1, 2, 0, 4, 5, 6]))
print(is_monotonic([5, 4, 3, 2]))







# Exercise 10
# Write a function that prints the longest word in a list.

def longest_word_in_a_list(list_of_words):
    longest_word = list_of_words[0]
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return f"The longest word in the list with {len(longest_word)} characters is: {longest_word}"


print(longest_word_in_a_list(["calabaza", "a", "asdasfgakhfg", "casa", "pretorian", "extremlylongcharacter"]))









# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
        

def sort_int_and_string(list_of_items):
    list_of_int = []
    list_of_str = []
    for element in list_of_items:
        if isinstance(element, str):
            list_of_str.append(element)
        elif isinstance(element, int):
            list_of_int.append(element)

    return f"The list of string is: {list_of_str} and the list of numbers is: {list_of_int}"




print(sort_int_and_string(["check", "if", "everithing", "get", "divide", 5, 6, 3, 7, 4.5, 3, 6, 23, True]))









# Exercise 12
# Write a function to check if a string is a palindrome:


def is_palindrome(word):
    word_reversed = word[::-1]
    if word == word_reversed:
        return True, "this word is palindrome"

    return False, "This word is not a palindrome"


print(is_palindrome("revers"))









# Write a function that returns the amount of words in a sentence with length > k:

def how_many_words_with_more_than_x_letters(list_of_words, x):
    how_many = 0
    list_of_words_get_condition = []
    for word in list_of_words:
        if len(word) > x:
            how_many += 1
            list_of_words_get_condition.append(word)

    return f"They are {how_many} word with more than {x} characters. The list of words: {list_of_words_get_condition}"



print(how_many_words_with_more_than_x_letters(["helo", "casa", "chillllll", "1234567890"], 2))







# Write a function that returns the average value in a dictionary (assume the values are numeric):

test_dictionary = {'a': 1,'b':2,'c':8,'d': 1}



def average_value_dictionary(dictionary):
    total = 0
    amount_of_items = len(dictionary)
    for item in dictionary:
        total += dictionary[item]
    
    return f"the average of the values of the items is: {total/amount_of_items}"



print(average_value_dictionary(test_dictionary))





# Write a function that returns common divisors of 2 numbers:

def comun_divisors_two_numbers(number1, number2):
    divisors_number_1 = []
    divisors_number_2 = []
    both_divisors = []
    for i in range(1, int(number1 / 2)):
        if number1 % i == 0:
            divisors_number_1.append(i)

    for i in range(1, int(number2 / 2)):
        if number2 % i == 0:
            divisors_number_2.append(i)

    if len(divisors_number_1) > len(divisors_number_2):
        for divisor in divisors_number_1:
            if divisor in divisors_number_2:
                both_divisors.append(divisor)

    if len(divisors_number_1) < len(divisors_number_2):
        for divisor in divisors_number_2:
            if divisor in divisors_number_1:
                both_divisors.append(divisor)
    
    return f"both numbers share this divisors {both_divisors}"


print(comun_divisors_two_numbers(1110, 3330))









# Exercise 16
# Write a function that test if a number is prime:





def is_prime(number):
    divisors_number = []
    
    for i in range(1, int(number / 2)):
        if number % i == 0:
            divisors_number.append(i)

    if len(divisors_number) == 1:
        return True


    return False, f"this are the divisors: {divisors_number}"



print(is_prime(171))











# Exercise 17
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weirdPrint([1,2,2,3,4,5])
#     >>>[2,4]

    

def even_index_and_number(list_of_numbers):
    list_of_numbers_to_return = []
    for i in range(len(list_of_numbers)):
        if i % 2 == 0 and list_of_numbers[i] % 2 == 0:
            list_of_numbers_to_return.append(list_of_numbers[i])
    
    
    return f"The list of numbers with even index and value are: {list(set(list_of_numbers_to_return))}"


print(even_index_and_number([1,2,3,4,5,6,7,8,9,11,12,14,15,56,5,43,45,6,44,52,54,44,31,34,30,32,33,33,33,3,3,3]))








# Exercise 18
# Write a function that accepts an undefined numbers of keyworded arguments and return the count of different types:

#     >>>TypeCount(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2




def count_types(**kwargs):
    amount_of_int = 0
    amount_of_float = 0
    amount_of_str = 0
    amount_of_bools = 0
    for k,v in kwargs.items():
        print(v)
        if isinstance(v, str):
            
            amount_of_str += 1
        elif isinstance(v, float):
            amount_of_float += 1
        elif isinstance(v, bool):
            print("bool")
            amount_of_bools += 1    
        elif isinstance(v, int):
            amount_of_int += 1
            print("int")
        
    return f"{amount_of_int} integers, {amount_of_float} floats , {amount_of_bools} booleans, {amount_of_str} strings"


print(count_types(a = 1, b = "string", c=1.0,  d = True, e = False))












