
# from numpy import random

# # Exercise 1 : Concatenate Lists
# # Write a script that concatenate two lists together without using the + sign.


# list_1 = [1,2,3,4,5]
# list_2 = [5,6,7,44,55]

# for item in list_2:
#     list_1.append(item)

# print(list_1)













# # Exercise 2: Greatest Number
# # Take three numbers from the user and print the greatest number.
# #     Test Data
# #     Input the 1st number: 25
# #     Input the 2nd number: 78
# #     Input the 3rd number: 87

# #     The greatest number is: 87
# list_of_numbers = []
# user_number = 0
# amount_item = 1
# how_many_numbers = input("how many numbers you want to compare: ")
# while amount_item <= int(how_many_numbers):  
#     user_number = input(f"Imput the {amount_item} number: ")
#     list_of_numbers.append(user_number)
#     amount_item += 1

    
# greatest_numer = max(list_of_numbers)

# print(f"The greatest number is {greatest_numer}")












# Exercise 3 : The Alphabet
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant


# alphabet = "abcdefghifklmnopqrstuvwxyz"

# for letter in alphabet:
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         print(f"the letter {letter} is a vowel")
#     else:
#         print(f"the letter {letter} is a consonant") 












# Exercise 4 :
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# 1. Write a script with the list of names provided. This code should ask the user for input
# * if the input exists in the list print the index of the first occurence
# Example: if input is ‘Cortana’ we should be printing the index 1




# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']


# check_location = input("Wich index you want to check: ")

# if check_location in names:
#     print("the index is:", names.index(check_location))












# Exercise 5 : Words And Letters
# Take 7 words as input from a user and store them for use in a list named words
# should not be done on 7 lines
# Mad props if you can do it in one :)
# Ask a single character input from the user and store it in a variable letter
# Tell the user what index letter is in each item in words
# If the letter doesn’t exist in a given word, print a friendly message saying so


# words = []
# word = ""
# for word in range(7):
#     word = input("tell me a word: ")
#     words.append(word)



# print(words)



# letter = input("tell me a character: ")

# for i in range (1,8):
#     if letter in words[i]:
#         index_ = words[i].index(letter)
#         print(f"the index of {letter} in {words[i]} is {index_}")
#     else:
#         print(f"{letter} was not found in {words[i]}")




    





# Exercise 6 :
# Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list 
# actually starts at one and ends at one million. Also,
#  use the sum() function to see how quickly Python can add a million numbers .




# list_of_first_million = []

# for i in range(1, 1000001):
#     list_of_first_million.append(i)

# max_number = max(list_of_first_million)
# min_number = min(list_of_first_million)
# sum_first_million = sum(list_of_first_million)
# print(f"the max number is: {max_number}")
# print(f"the min number is: {min_number}")
# print(f"the sum is {sum_first_million}")













# Exercise 7 :
# Write a program which accepts a sequence of comma-separated numbers from the
#  console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# list_of_number = input("put numbers separated by ',': ")
# list_of_list = list_of_number.split(",")
# tuple_of_list = tuple(list_of_list)

# print(list_of_list)
# print(tuple_of_list)









# Exercise 8 : Random Number
# Accept input from a user if its between 1 and 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# Print a message if the user guessed the correct number or not.
# Bonus: use a menu to let the user keep guessing until he wants to quit
# Bonus 2: on exit tally up and display total games, wins and losses





# exit_code = ""
# number_to_guess = 0
# while exit_code != "exit":
#     number_to_guess = random.rand()



# i was not able to download numpy i have to check and solve that















# Exercise 9: Check Please !
# Your code will print out the bill for a customer, with the help of the waiter/waitress.

# First, ask some questions, and then print out the bill.
# Store the answers to the questions in variables, so that they can be used later on in your code.
# Ask the user (waiter) for each of these pieces of information, 
# assuming that the customer ordered only one item (but multiple orders of the same item are allowed):
# Hint: a menu like from Exercise 7 of the XP may be helpful here
# a. The customer’s name (this is a friendly bar!).
# b. The name of the waiter/waitress.
# c. The name of the item (eg. ‘beer’).
# d. The price of the item.
# e. The amount of items that were ordered (eg. 3, when the customer had 3 beers)
# f. The discount amount (user should input zero if there was no discount).
# Now calculate the total to charge the customer.
# Bonus: add VAT to the total.
# Print out a nicely formatted bill for the user, on multiple lines.
#  Add some lines of stars or hyphens to create the effect of a “border” or “line”, to make it look more professional.
# Use at least one multi-line string in your output. Use string formatting (f-strings)



costumer_name = input("what is the costumer name: ")
waiter_name = input("what is the waiter/s name: ")
item_name = ""
item_price = 0
amount_of_items = 0
discount_on_item = 0
total_bill = 0
item_sub_total = 0

amount_of_items_in_the_bill = int(input("How many items have the bill? :"))
list_of_items = []
list_of_prices = []
list_of_amounts = []
list_of_discount = []
list_of_subtotals = []


for item in range(1,amount_of_items_in_the_bill+1):
    item_name = input("Item name: ")
    item_price = int(input(f"{item_name} price? : "))
    amount_of_items = int(input(f"How many {item_name} "))
    discount_on_item = int(input(f"{item_name} have discount? how much? "))
    item_sub_total = (item_price * amount_of_items) - (discount_on_item * item_price)
    total_bill += item_sub_total
    list_of_items.append(item_name)
    list_of_prices.append(item_price)
    list_of_amounts.append(amount_of_items)
    list_of_discount.append(discount_on_item)
    list_of_subtotals.append(item_sub_total)
    if item == amount_of_items_in_the_bill:
        print(f"* Costumer name: {costumer_name}")
        print(f"* The waiter/s is : {waiter_name}")
        print('''
* The Bill
* item Amount  Name         Price   discount   subtotal   ''')

        for i in range(amount_of_items_in_the_bill):
            print(f'* {i}    {list_of_amounts[i]}         {list_of_items[i]}       {list_of_prices[i]}       {list_of_discount[i]}        {list_of_subtotals[i]}')
        print(f"The total amount of the bill is: \n       {total_bill}")


    






