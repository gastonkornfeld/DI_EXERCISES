import math


# Exercise 1: Formula
# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# We will take a comma-separated string of numbers from the
#  user, then, use each number from the user as D in the formula and return all the results
# For example, let’s assume the following comma separated input sequence is given to the program: 100,150,180
# The output of the program should be:

# 18,22,24



def calculation(number1, number2, number3):
    q1 = int(math.sqrt((2 * 50 * number1)/30))
    q2 = int(math.sqrt((2 * 50 * number2)/30))
    q3 = int(math.sqrt((2 * 50 * number3)/30))
    return f"{q1}, {q2}, {q3}"


print(calculation(100,150,180))










# Exercise 2 : List Of Integers
# We are given a list of 10 integers to analyze. Repeat the questions below with the following lists of numbers:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
# We will now print some information about the list of numbers. Each time, 
# print the answer together with a helpful message that tells the user what you are printing.

# Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers

# A list containing the first and the last numbers only.
# A list of all the numbers greater than 50.
# A list of all the numbers smaller than 10.
# A list of all of the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# The numbers without any duplicates – also print how many numbers are in the new list.
# The average of all the numbers.
# The largest number.
# 10.The smallest number.
# 11.Bonus: Find the sum, the average the largest and smallest number without using builtin functions.
# 12.Extra bonus: instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
# a. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each answer from the user should be added onto a list variable that you created earlier.
# b. After asking the user 10 times, you should now have a list of integers.
# c. Print a line to separate the input section (getting the numbers from the user) from the output section).




list_1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
list_2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
list_3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
list_4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

def list_of_numbers(list_of):
    return str(list_of.copy())


def sorted_reverser(list_of_numbers):
    list_sorted = sorted(list_of_numbers)
    list_sorted = list_sorted[::-1]
    return list_sorted
    
def sum_list_numbers(list_of_numbers):
    return sum(list_of_numbers)    

def only_firs_and_last(list_of_numbers):
    return f"{list_of_numbers[0]} is the first, and {list_of_numbers[-1]} is the last number on the list"

def only_greater_than_50(list_of_numbers):
    list_with_the_condition = [number for number in list_of_numbers if number > 50]
    return list_with_the_condition

def only_smaller_than_10(list_of_numbers):
    list_with_the_condition = [number for number in list_of_numbers if number < 10]
    return list_with_the_condition

def squares_of_all_numbers(list_of_numbers):
    list_with_the_condition = [number**2 for number in list_of_numbers]
    return list_with_the_condition

def no_duplicates(list_of_numbers):
    list_with_the_condition = [number for number in list_of_numbers if list_of_numbers.count(number) < 2]
    return list_with_the_condition, f"They are {len(list_with_the_condition)} items in the list"


def average(list_of_numbers):
    total = sum(list_of_numbers)
    average = total/len(list_of_numbers)
    return average

def max_and_min(list_of_numbers):
    return f"The max number is {max(list_of_numbers)}, and the minimum number on the list is {min(list_of_numbers)}"



print(list_of_numbers(list_1))

print(sorted_reverser(list_1))

print(sum_list_numbers(list_1))

print(only_firs_and_last(list_1))

print(only_greater_than_50(list_1))

print(only_smaller_than_10(list_1))

print(squares_of_all_numbers(list_1))

print(no_duplicates(list_1))

print(average(list_1))

print(max_and_min(list_1))





# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it into your code, and store it as a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…)
# How many sentences it contains
# How many words it contains
# How many unique words it contains
# Bonus: How many non-whitespace characters it contains
# Bonus: The average amount of words per sentence in the paragraph
# Bonus: the amount of non-unique words in the paragraph


frase = '''
less TV, more reading.
less shopping, more outdoors.
less clutter, more space.
less rush, more slowness.
less consuming, more creating.
less junk, more real food.
less busywork, more impact.
less driving, more walking.
less noise, more solitude.
less focus on the future, more on the present.
less work, more play.
less worry, more smiles.
breathe'''
print(frase)
print(f"The phrase contain {len(frase)} characters")
sentences = frase.split(".")
print(f"The amount of sentences is {len(sentences)}")
words = frase.split(" ")
print(f"The amount of words is {len(words)}")
words_unique = list(set(words.copy()))
print(f"The amount of unique words is {len(words_unique)}")

# Bonus
non_whitespaces = [char for char in frase if char != " "]
print(f"The amount of non-whitespaces characters is {len(non_whitespaces)}")
average_word_per_sentence = len(words)/len(sentences)
print(f"The average of words per sentence is {round(average_word_per_sentence,2)}")
non_unique_words = list(set([word for word in words if words.count(word) > 1 ]))
print(f"The amount of non unique words is {len(non_unique_words)}")











# Exercise 4
# Write a program to compute the frequency of the words from the input.
# Tip: The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
# #     to:1


phrashe_to_count_words = input("Thell me a phrase to count his words: \n")

list_of_words = phrashe_to_count_words.split()
list_without_repetition = list(set(list_of_words.copy()))
list_of_amount_of_each_word = []
list_without_repetition.sort()

for item in list_without_repetition:
    item_amount = list_of_words.count(item)
    list_of_amount_of_each_word.append(item_amount)


Final_input_of_information = dict(zip(list_without_repetition, list_of_amount_of_each_word))
for item in Final_input_of_information:
    print(f"{item}: {Final_input_of_information[item]}")   








