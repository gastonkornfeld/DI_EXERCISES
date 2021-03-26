# Randomizes a number (range 0..100), then prints all the even numbers from 0 to the randomized.

# Exercise 1: List Of Integers - Randoms
# !! This is the continuation of the Exercise Week4Day2/Exercise 2 XP NINJA !!
# 2. Instead of asking the user for 10 integers, generate 10 random integers yourself.
#  Make sure that these random integers lie between -100 and 100.
# 3. Instead of always generating 10 integers, let the amount of integers also be random!
#  Generate a random positive integer no smaller than 50.
# 4. Go back and check all of your output! Does your code work correctly for a list of unknown length, 
# or does it only work correctly for a list that has 10 items in it?
# 5.
import random

def random_evens_numbers():
    amount_of_numbers = random.randint(50, 200)
    list_of_numbers = []
    for i in range(amount_of_numbers):
        number = random.randint(-100, 100)
        if number % 2 == 0:
            list_of_numbers.append(number)
    return list_of_numbers
    

# print(random_evens_numbers())




# Exercise 2: Authentication CLI - Login:
# Create a menu using a while loop and user input (see week 4 day 2 exercise xp7)
# Create a dictionary that contains users: each key will represent a username, 
# and each value will represent that users’ password. Start this dictionary with 3 users & passwords
# Add a menu option to exit
# Add a menu option called login: when a user selects login, take 2 inputs from 
# him and check if they match up with any users in our dictionary
# Print a message on if they logged in successfully or not
# If successful try and store the username in a variable called logged_in so we can track it later


users = {
    "gaston" : "12345",
    "natalia" : "natalia",
    "diego" : "diego"
}

menu_exit = True
user_is_login = False
while menu_exit:
    menu_option = input("exit or login?\n")
    if menu_option == "exit":
        menu_exit = False
        break
    elif menu_option == "login":
        print("Welcome, Input Username and pasword\n")
        username = input("Username: ")
        password = input("Password: ")
        
        for user in users:
            if username == user:
                if password == users[user]:
                    user_is_login = True
                    print("now you are logged in")
                    menu_exit = False
                else:
                    print("wrong Password")
        if not user_is_login:
            print("Login didnt work")   
    else:
        print("please input login or exit")



