




# # Exercise 1 : Convert Lists Into Dictionaries
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method
# # Expected output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dictionary = zip(keys, values)
# print(dict(dictionary))









# # Exercise 2 : Cinemax #2
# # “Continuation of Exercise Cinemax of Week4Day2 XP”

# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free
# # if they are between 3 and 12, the ticket is $10;
# # and if they are over age 12, the ticket is $15 .
# # Here is the object you will work with : family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# # Using a for loop, the dictionary above, and the instructions,
# #  print out how much each family member will need to pay alongside their name
# # After the loop print out the family’s total cost for the movies
# # Bonus: let the user input the names and ages instead of using the 
# # provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)

# total_cost = 0
# subtotal = 0
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# family_ages = list(family.values())
# family_members = list(family.keys())



# for costumer_number in range(len(family_members)):
#     if family_ages[costumer_number] < 3:
#         print(f"{family_members[costumer_number]} Dont pay, have less than 3 years old")
#     elif 3 < family_ages[costumer_number] <= 12:
#         print(f"{family_members[costumer_number]} Pay $10")
#         subtotal = 10
#         total_cost = total_cost + subtotal
#     else:
#         print(f"{family_members[costumer_number]} Pay $15")
#         subtotal = 15
#         total_cost = total_cost + subtotal

# print(f"The total cost for the family is: ${total_cost}")

# # bonus
# total_cost2= 0
# subtotal2 = 0

# family2 = dict()
# print(family2)

# actual_member = ""
# age = 0
# while actual_member != "exit":
#     actual_member = input("(exit to finish) Tell me the name of the family member: ")
#     if actual_member == "exit":
#         break
    
#     age = int(input("what is the age of your family member: "))
#     family2[actual_member] = age
#     print(family2)


# family_ages2 = list(family2.values())
# family_members2 = list(family2.keys())

# for costumer_number2 in range(len(family_members2)):
#     if family_ages2[costumer_number2] < 3:
#         print(f"{family_members2[costumer_number2]} Dont pay, have less than 3 years old")
#     elif 3 < family_ages2[costumer_number2] <= 12:
#         print(f"{family_members2[costumer_number2]} Pay $10")
#         subtotal2 = 10
#         total_cost2 = total_cost2 + subtotal2
#     else:
#         print(f"{family_members2[costumer_number2]} Pay $15")
#         subtotal2 = 15
#         total_cost2 = total_cost2 + subtotal2

# print(f"The total cost for the family is: ${total_cost2}")











# # Exercise 3: Zara
# # Here is some information about a brand.
# # name: Zara 
# # creation_date: 1975 
# # creator_name: Amancio Ortega Gaona 
# # type_of_clothes: men, women, children, home 
# # international_competitors: Gap, H&M, Benetton 
# # number_stores: 7000 
# # major_color: France -> blue, Spain -> red, US -> pink, green 
# # Create a dictionary called brand, and translate the information above into keys and values.
# # Change the number of stores to 2.
# # Print a sentence that explains who the clients of Zara are.
# # Add a key called country_creation with a value of Spain to brand
# # If the key international_competitors is in the dictionary, add the store Desigual.
# # Delete the information about the date of creation.
# # Print the last international competitor.
# # Print in a sentence, the major clothes’ colors in the US.
# # Print the amount of key value pairs (length of the dictionary).
# # Print only the keys of the dictionary.
# # Create another dictionary called more_on_zara with the following information:

# # creation_date: 1975 
# # number_stores: 10 000 
# # Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# # Print the value of the key number_stores. What just happened ?


# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": [("France", "blue"), ("spain", "red"), ("US", ["pink", "green"]) ]

# }








# brand["number_stores"] = 2

# lengt_of_list = len(brand["type_of_clothes"])

# for i in range (lengt_of_list):
#     print("zara sell clothes for: ", brand["type_of_clothes"][i])



# if brand["international_competitors"] != None:
#     brand["international_competitors"].append("Desigual")




# brand["Country_creation"] = "Spain"



# brand.pop("creation_date")



# print(brand["international_competitors"][-1])





# colors_in_US1 = brand["major_color"][2][1][0]
# colors_in_US2 = brand["major_color"][2][1][1]
# print(f"The major colours in US are {(colors_in_US1)} and {colors_in_US2}")


# amount_of_keys = len(brand.keys())
# print(f"The amount of items are: {amount_of_keys}")


# for key in range (amount_of_keys):
#     print(f"The key number {key} is {list(brand.keys())[key]}")


# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,

# }


# new_dictionary = brand.copy()
# new_dictionary.update(more_on_zara)

# print(new_dictionary["creation_date"])








# Exercise 4 : Disney Characters
# Consider this list :

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
# Analyse these results :

#1/ print(disney_users_A) >> {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/ print(disney_users_B) >> {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ print(disney_users_C) >> {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a for loop to recreate the #1 result. Tip : don’t hardcode the numbers
# Use a for loop to recreate the #2 result. Tip : don’t hardcode the numbers
# Use a method to recreate the #3 result
# Hint: The 3rd result is in the alphabetical order
# Recreate the #1 result, only if:
# The characters’ names contain the letter “i”.
# The characters’ names start with the letter “m” or “p”.


users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
numbers = [num for num in range(len(users)) ]

disney_users_A = dict(zip(users, numbers))
print(disney_users_A)

disney_users_B = dict(zip(numbers, users))
print(disney_users_B)

users_C = users.copy()
users_C.sort()
print(users_C)

disney_users_C = dict(zip(users_C, numbers))
print(disney_users_C)



users_with_condition1 = [user for user in users if "i" in user ]
numbers_condition1 = [num for num in range(len(users_with_condition1)) ]

disney_users_condition1 = dict(zip(users_with_condition1, numbers_condition1))
print(disney_users_condition1)



users_with_condition2 = [user for user in users if user[0] == "M" or user[0] == "P"]
numbers_condition2 = [num for num in range(len(users_with_condition2)) ]

disney_users_condition2 = dict(zip(users_with_condition2, numbers_condition2))
print(disney_users_condition2)


