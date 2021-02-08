


# Exercise 1 : Hello World
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello 


print("hello world \nhello world \nhello world \nhello ")


# Exercise 2 : Some Math
# Calculate the result of: (99^3) * 8

result_exercise_2 = 99 ** 3 * 8
print("The result is: ", result_exercise_2)



# Exercise 3 : What Is The Output ?
# Predict the output of the following code snippets:
# >>> 5 < 3    # False
# >>> 3 == 3    #True
# >>> 3 == "3" #False
# >>> "3" > 3  #True  #is an error in the beggining thougth about. 
# >>> "Hello" == "hello" #false



# Exercise 4 : Your Computer Brand
# Create a variable called computer_brand that contains the brand of your computer.
# Insert and print the above variable in a sentence,like "I have a razer computer".


computer_brand = "Asus"
print(f"I have an {computer_brand} computer")





# Exercise 5: Your Information
# Create a variable called name, and give it your name as a value (text)
# Create a variable called age, and give it your age as a value (number)
# Create a variable called shoe_size, and give it your shoe size as a value
# Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
# Have your code print the info message.
# Run your code


name = "Gaston Kornfeld"
age = 32
shoe_shize = 41
info = "well I am " + name + " I was born the 2 of december of 1988 so i have " + str(age) + " years old, I am not so tall i am 1,71m so my shoe size is " + str(shoe_shize)

print(info)

# Exercise 6 : A & B
# Given two variables a and b that you need to define, make a program that print Hello World only if a is greater than b.


variable_a = 79
variable_b = 78

if variable_a > variable_b:
    print("hello world")


# Exercise 7 : Odd Or Even
# Write a script that asks the user for a number and determines whether this number is odd or even.

user_number =  input("Please give me a number: ")
user_number = int(user_number)
if user_number % 2 == 0:
    print("you give me an even number")
else:
    print("you give me an odd number")


# Exercise 8 : What’s Your Name ?
# Write a script that asks the user for his name and 
# determines whether or not you have the same name, print 
# out a funny message based on the outcome



user_name = input("I will ask you to tell me your name please: ")

if user_name == name:
    print("Amazing we have the same name")
else :
    print("My name is "+ name + ", well " + user_name + " I think we have a similar name, depends how you look at it. Im shure we share some vowels there")




# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Write a script that will ask the user for their height in inches, print a message if
#  they can ride a roller coaster or not based on if they are taller than 145cm
# Please note that the input is in inches and you’re calculating vs cm, you’ll need to convert your data accordingly



user_height_in_inches = input("Tell me your height in inches: ")
user_height_in_inches = float(user_height_in_inches)

user_height_in_cm = user_height_in_inches * 2.54

if user_height_in_cm < 145:
    print("you are not enough tall to ride")
else:
    print("Welcome to the ride")





