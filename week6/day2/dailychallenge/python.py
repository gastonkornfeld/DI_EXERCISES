import random


# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod

user_string = ""

while len(user_string) != 10:
    user_string = input("write a string containing exactly 10 carhacters: ")
    if len(user_string) < 10:
        print("string not long enough")
    elif len(user_string) > 10:
        print("string too long")


print("First character: ", user_string[0])
print("last character: ", user_string[-1])

list_of_characters = []
test = ""

for letter in user_string:
    test = test + letter
    print(test)
    list_of_characters.append(letter)





random.shuffle(list_of_characters)

print(''.join(list_of_characters))




    



     