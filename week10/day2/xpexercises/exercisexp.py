import string
import pyjokes
import random
import sys

argv = sys.argv
try:
    first_number = argv[1]
    second_number = argv[2]
    print(first_number, second_number)
except:
    first_number = 0
    second_number = 100
# import functions
# from functions import addOperator
# from functions import substractOperator as subs
# import datetime as date


def between_0_and_100():
    number = -1
    while not (0 <= number <= 100):
        
        number = int(input("write a number between " + str(first_number) + " and " + str(second_number) + " lets see if i can matched:\n"))
        computer_number = random.randint(int(first_number),int(second_number))
    if number == int(computer_number):
        print("amazing")
        return "good job" 
    else:
        print(f"your number: {number}, computer number: {computer_number}")
        between_0_and_100()


print(between_0_and_100())







# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. 
# No numbers and a special symbol.
# Hint: use the string module


# def string_5_random_ascci():
        
#     random_word = "".join(random.sample(string.ascii_letters, 5))
#     return random_word


# print(string_5_random_ascci())


# print(pyjokes.get_joke())



