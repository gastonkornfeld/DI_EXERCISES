





# # exercise 1: Birthday Look-Up
# # Create a variable called birthdays. Its value should be a dictionary.
# # Initialize this variable with birthdays of 5 people of your choice. 
# # For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday.
# #  Tip : Use the format “YYYY/MM/DD”.
# # Print a welcome message to the user. Then tell him: “You can look up the birthday of the people in the list!”“
# # Ask the user to give you a person’s name and store his answer in a variable.
# # Get the birthday for the person’s name from the birthdays dictionary.
# # Print out the birthday with a nicely-formatted message.

# # Exercise 2: Birthdays Advanced
# # Before asking the user to type in a person’s name, print out all of the names from the dictionary, 
# # to make it easier for them to choose.
# # If the person that the user types is not found in the dictionary, print an error message
# #  (“Sorry, we don’t have birthday information for “”)

# # Exercise 3: Add Your Own Birthday
# # Insert this new code: before you offer the user to type a person’s name to look up, ask the user to add a birthday first:
# # Ask the user for a person’s name – store it in a variable
# # Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# # Now add this new data into your dictionary.
# # The rest of your code should follow (from Exercise 2).
# # Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.



# birthdays = {
#     "noam": "02/12/1988",
#     "alisa": "23/03/1966",
#     "grace": "28/02/1954",
#     "chaim": "08/11/1944",
#     "ramsy": "22/08/2000",

# }
# print("well lest first add a birthday to the birthday dictionary")
# new_birthday_Name = input("what is the name og the person you want to add?: \n")
# new_birthday_date = input(f"what is the birthday of {new_birthday_Name}, Use the format DD\MM\YYYY: \n")

# birthdays[new_birthday_Name] = new_birthday_date

# print("Welcome, You can look up the birthday of the people in this list")

# birthday_persons = list(birthdays.keys())
# for person in birthday_persons:
#     print(person)

# wich_birthday = input("wich name you want to chek the birthday: \n")
# if wich_birthday in birthdays:
#     print(f"So the birthday of {wich_birthday} is {birthdays[wich_birthday]} ")
# else:
#     print(f"Sorry we dont have birthday information for {wich_birthday} ")














# Exercise 4: Fruit Shop:
# Create a new dictionary called items and add the following key-value pairs to it using code.
#  They each represent an item and its price
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# Print all the items and their prices in your dictionary in a human-readable way
# Add stock information to each item (keep track of how many of each item our shop has).
# Once you’ve added stock info to the item,
#  write some code to figure out how much it would cost to buy your entire stock of all items





# items = dict()
# items["banana"] = 4
# items["apple"] = 2
# items["orange"] = 1.5
# items["pear"] = 3

# fruits = list(items.keys())
# prices = list(items.values())

# for i in range(len(fruits)):
#     print(f"The price of the {fruits[i]} is ${prices[i]} the kilogram \n")


# total = sum(prices)
# print(f"The total is {total} for a kilogram of each")









# Exercise 5 : Cars
# Copy the following string into your script: “Volkswagen, Toyota, Ford Motor, Honda, Chevrolet”
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
# Print out the above information with meaningful output messages.
# Bonus: There are a few duplicates in this list [“Honda”,”Volkswagen”, “Toyota”, “Ford Motor”, “Honda”, “Chevrolet”, “Toyota”]:
# Remove these programmatically. (Hint: you can use sets to help you).
# Print out the companies without duplicates, in a comma-separated list 
# with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), and also print out a message
#  saying how many companies are now in the list.
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.


companies = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
companies_in_a_list = companies.split(",")

print(f"They are {len(companies_in_a_list)} Companies")

companies_in_a_list2 = companies_in_a_list.copy()
companies_in_a_list2.sort()
companies_in_a_list2.reverse()
print(companies_in_a_list2)

how_many_with_o = [company for company in companies_in_a_list if "o" in company]
print(f"They are {len(how_many_with_o)} companyes with letter 'o'")

how_many_not_with_i = [company for company in companies_in_a_list if "i" not in company]
print(f"They are {len(how_many_not_with_i)} companyes without letter 'i'")




companies_2 = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
companies_2_no_repeat = list(set(companies_2))
how_many = len(companies_2_no_repeat)
companies_2_display = ", ".join(companies_2_no_repeat)

print(f"the list of companies without repetition is {companies_2_display} and they are now {how_many} companies")


# Bonus

companies_in_a_list3 = companies_in_a_list.copy()
companies_in_a_list3.sort()
companies_in_a_list4 = [company[::-1] for company in companies_in_a_list3 ]
companies_4_display = ", ".join(companies_in_a_list4)

print(f"the list of companies in A-Z order and backward is{companies_4_display}")

