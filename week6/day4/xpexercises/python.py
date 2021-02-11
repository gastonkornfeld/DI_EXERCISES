


# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers



# my_fav_numbers = {2, 7, 27, 22, 227}

# my_fav_numbers.add(3)
# my_fav_numbers.add(8)
# my_fav_numbers.remove(227)
# print(f"my fav numbers are: \n {my_fav_numbers}")

# friend_fav_numbers = {3, 45, 65, 3, 2, 1, 32, 7}
# print(f"my friend fav numbers are: {friend_fav_numbers}")
# our_fav_numbers = my_fav_numbers
# our_fav_numbers.update(friend_fav_numbers)
# print(f"our favorites numbers are: {our_fav_numbers} ")
















# Exercise 2: Tuple
# Given a tuple with integers is it possible to add more integers to the tuple?
# answer: it is no possible to modify or add any value to a tuple ones it was created.

















# Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive.

# for number in range(21):
#     print(number)
















# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.


# number_to_append = 1.0
# list_of_floats = []

# for i in range (8):
#     number_to_append += 0.5
#     list_of_floats.append(number_to_append)

# print(list_of_floats)






















# Exercise 5: Shopping List
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# basket.remove("Banana")
# print(basket)
# basket.pop(2)
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)

# print(basket.count("Apples"))

# basket.clear()
# print(basket)

















# Exercise 6 : Loop
# Write a while loop that will keep asking the user for input until the input is the same as your name.

# only_my_name = ""

# while only_my_name != "gaston":
#     only_my_name = input("guess my name to continue: \n")

# print("correct")





















# Exercise 7
# Given a list, use a while loop to print out every element which has an even index.

# item = 0
# list_to_chek = [2,4, 55,66,77,88,77,66,55,55,55,55,55, 3, 4, 5, 6, 7, 8, 9, 33, 44, 32, 21, 10]
# print(list_to_chek)
# amount_of_items = len(list_to_chek)
# while item < amount_of_items:
#     if item % 2 == 0:
#         print(list_to_chek[item])
#     item += 1




















# # Exercise 8
# # Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
    
# list_of_multiples_of_3 = []

# for multiple_of_3 in range(1, 11):
#     list_of_multiples_of_3.append(multiple_of_3*3)


# print(list_of_multiples_of_3)























# Exercise 9
# Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.



# multiples_of5_and_divisible_by_7 = []



# for number in range(1500, 2700):
#     if number % 7 == 0 and number/5 == int(number/5):
#         multiples_of5_and_divisible_by_7.append(number)


# print(f"the numbers between (1500-2700) that are multiple of 5 and divisible for 7 are: \n {multiples_of5_and_divisible_by_7}")























# Exercise 10: Favorite Fruits
# Ask the user to type in his/her favorite fruit(s) (one or several fruits).
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# Now that we have a list of fruits, ask the user to type in the name of any fruit.
# If the user’s input is a fruit name existing in the list above,
#  print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT a fruit name existing in the list above, 
# print, “You chose a new fruit. I hope you enjoy it too!”.
# Bonus: Display the list in a user friendly way :
#  add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!


# user_favourites_fruits = input("Please add your favourites fruits separate by space: \n")

# list_of_fruits = user_favourites_fruits.split(" ")

# new_user_fruit = input("Now ask me about a fruit: \n")

# if new_user_fruit in list_of_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy it too!")



















# Exercise 11: Who Ordered A Pizza ?
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exit print all the toppings on the pizza and what the total is (10 + 2.5 for each topping)



# user_topping = ""
# pizza_price = 10
# list_of_toppings = []

# while user_topping != "quit":
#     user_topping = input("Wich topping you would like to add to your pizza(write quit to finish): ")
#     if user_topping == "quit":
#         break
#     else:
#         print(f"we will ad {user_topping} to your pizza")
#         pizza_price += 2.5
#         list_of_toppings.append(user_topping)


# print(f"the total price is {pizza_price}")
# print(f"your toppings are {list_of_toppings}")






















# Exercise 12: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.


# ticket_price = 0
# total = 0
# member_age = ""

# while member_age != "end":
#     member_age = input("(write end to finish) What is the age of the person that wants the ticket: ")
#     if member_age == "end":
#         break
#     if int(member_age) < 3:
#         print("Under age of 3 dont pay.")
#     elif  3 <= int(member_age) <= 12:
#         print("The price for your ticket is $10")
#         total += 10
#     else:
#         print("The price for your ticket is $15")
#         total += 15

# print(f"the total is: {total}")


# name = ""
# list_of_allowed = []
# member_age = ""

# while member_age != "end":
#     member_age = input("(write end to finish) What is the age of the person that wants the ticket: ")
#     if member_age == "end":
#         break
#     if  16 <= int(member_age) <= 21:
#         print("You are allowed to watch the movie")
#         name = input("Tell me your name: ")
#         list_of_allowed.append(name)
        
#     else:
#         print("Your age is not allowed for this movie, I am sorry")
        

# print(f"the List of allowed people is {list_of_allowed}")



















# Exercise 13 : Who Is Under 16?
# This time you have a list of users, and you want to remove every user that is below 16 years old.

# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.





# list_of_users= ["andrea", "paul", "marcos", "ivan", "carlos"]

# member_age = ""

# for name_user in list_of_users:
#     print(f"hello {name_user} ")
#     member_age = input("what is your age: ")
#     if int(member_age) < 16:
#         list_of_users.remove(name_user)
    
        

# print(f"the List of under 16 is {list_of_users}")





















# Exercise 14: Family Members
# Using a while loop keep asking a user for input, these inputs will be used to control a menu
# On the menu we will have 4 options:
# Add a name
# If the user selects this ask for the name to add
# Remove an existing name
# If the user selects this ask for the name to remove
# View family members
# Print a nice list of the family members names
# Exit


family_member = ""
user_selection = ""
family_members = []
while user_selection != "exit":
    user_selection = input("Options: (exit: finish and print), (add: add a family member),\n (remove: remove a family member) (view: view the current family) : \n ")
    if user_selection == "exit":
        print(family_members)
    elif user_selection == "add":
        family_member = input("what is the name you want to add to the family:\n ")
        family_members.append(family_member)
    elif user_selection == "remove":
        family_member = input("what is the name you want to remove from the family:\n ")
        if family_member in family_members:
            family_members.remove(family_member)
        else:
            print("your name is not in the list, can not be removed\n ")
    elif user_selection == "view":
        print(family_members)
    else:
        print("This is not a correct option, choose add, remove, view or exit\n ")



    


