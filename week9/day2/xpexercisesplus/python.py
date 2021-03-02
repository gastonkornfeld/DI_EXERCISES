
import random



# Exercise 4 : Family
# Write a Family class and implement the following attributes:

# members: list of dictionaries with the keys name, age and gender (‘Male’/’Female’) and is_child.
# last_name (string)
# Initial members data:
# [ {'name':'Michael','age':35,'gender':'Male','is_child':False}, 
# {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]
# Implement the following methods:

# 
# is_18: accept the name of one member and returns True if he is over 18, False otherwise
# a method that nicely presents the family (use the info you find relevant)


class Family():

    def __init__(self):
        self.members = []


    def add_member(self, name, age, gender, is_child):
        new_member = {}
        new_member["name"] = name
        new_member["age"] = age
        new_member["gender"] = gender
        new_member["is_child"] = is_child
        self.members.append(new_member)
# born: adds a child to the members list (look up **kwargs), don’t forget to print a Congratulation message
#       
    def born(self, **kwargs):
        new_member = {}
        print("congratulations")
        new_member["gender"] = random.choice(["Male", "Female"])
        print(f"It is a {new_member['gender']}")
        new_member["name"] = input("How do you want to call your baby: ")
        new_member["is_child"] = True
        new_member["age"] = 0
        self.members.append(new_member)
        print(f"{new_member['name']} has born, it is a {new_member['gender']}")

# is_18: accept the name of one member and returns True if he is over 18, False otherwise
    def is_18(self, member_of_family):
        for i in range(len(self.members)):
            
            if self.members[i]["name"] == member_of_family:
                if self.members[i]["age"] >= 18:
                    return True
                elif self.members[i]["age"] < 18:
                    return False
            return "didnt fin the name in the list"


    def Presentfamily(self):
        print("this are the family members")
        for item in self.members:
            print(f'{item["name"]} {item["age"]} years old, {item["gender"]}')

family1 = Family()

# family1.add_member("Michael", 35, "Male", False)
# family1.add_member("Shara", 32, "Female", False)
# # family1.born()
# print(family1.members)
# print(family1.is_18("Gaston"))
# family1.Presentfamily()

# Exercise 5 : TheIncredibles Family
# Write a TheIncredibles class that inherits from the Family class:
# It is an Incredible Family, so they have powers, therefore the dictionaries
#  get new keys called power and incredible_name
# implement a method use_power, that prints the power of a member only if the said member is over 18
# if the member isn’t over 18 raise an Exception (check how !!) saying (‘You have no power here !!’)
# add a incredible_presentation method to present them with their incredible names and powers
# Look up the names of The Incredibles characters on google and build the family 
# (if you don’t find some information just improvise). Excluding baby jack !
# Print their normal presentation and their incredible presentation
# Use the ‘born’ method inherited from the family class to add Baby Jack with the power: “Unknown Power”
# Print both presentations again to check Baby Jack is born and that his power
#  is showing when using the incredible representation

class TheIncredibles(Family):

    def __init__(self):
        self.familyName = "The incredibles"
        self.incrediblesmembers = []


    def add_member(self, incredible_name, age, gender, power):
        new_member = {}
        new_member["incredible-name"] = incredible_name
        new_member["age"] = age
        new_member["gender"] = gender
        # new_member["is_child"] = is_child
        new_member["power"] = power
        print(new_member)
        self.incrediblesmembers.append(new_member)

    def Presentincrediblefamily(self):
        print(self.familyName)
        for item in self.incrediblesmembers:
            print(f'{item["incredible-name"]} {item["age"]} years old, {item["gender"]} powers: {item["power"]}')

    # def is_18(self, member_of_family):
    #     for i in range(len(self.members)):
            
    #         if self.members[i]["incredible-name"] == member_of_family:
    #             if self.members[i]["age"] >= 18:
    #                 return True
    #             elif self.members[i]["age"] < 18:
    #                 return False
    #         return "didnt fin the name in the list"

    def UsePower(self, incredible):
        
        
        for item in self.incrediblesmembers:
            
            if item["incredible-name"] == incredible:                
                if item["age"] >= 18:
                    power_use = random.choice(item["power"])
                    
                    print(f'{incredible} use {power_use}')
                    # return True
                elif item["age"] < 18:
                    print("you need to wait until 18 to use your powers")
                    # return False
            # return "didnt fin the name in the list"


    def born(self, **kwargs):
        new_member = {}
        print("congratulations")
        new_member["gender"] = random.choice(["Male", "Female"])
        print(f"It is a {new_member['gender']}")
        new_member["incredible-name"] = input("How do you want to call your baby: ")
        new_member["age"] = 0
        new_member["power"] = ["unknow"]
        self.incrediblesmembers.append(new_member)
        print(f"{new_member['incredible-name']} has born, it is a {new_member['gender']}, powers: {new_member['power']}")

familyinc = TheIncredibles()

familyinc.add_member("INCREDIBLE", 35, "Male",  ["SUPER-STRENGHT"])
familyinc.add_member("ELASTIGIRL", 32, "Female",  ["BODY-ELASTICITY"])
familyinc.add_member("VIOLET", 16, "Female", ["INVISIBILITY", "FORCE-FIELDS"])
familyinc.add_member("DASH", 13, "Male",  ["SUPER-SPEED"])
familyinc.Presentincrediblefamily()
familyinc.UsePower("VIOLET")
familyinc.UsePower("ELASTIGIRL")
familyinc.UsePower("DASH")
familyinc.UsePower("INCREDIBLE")
# print(family1.members)

familyinc.born()
familyinc.Presentincrediblefamily()