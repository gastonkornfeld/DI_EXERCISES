import random
# Vaccines Management System
# Your goal is to create a program to help a city with the vaccination of its citizens.








# Part 1
# You will have to create two classes:

# Human
# Queue
# Here is a description of them:

# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.











# 1) Human
# Represents a citizen of the city, it has the following attributes: 
# id_number (str), name (str), age (int), prioritary (bool) and blood_type (str).
#  Its blood type can be “A”, “B”, “AB” or “O”.

# It got no methods.

class Human():
    humanNumber = 1
    def __init__(self, name, age, blood_type):
        self. name = name
        self.age = age
        self.id_number = Human.humanNumber
        self.family = []
        Human.humanNumber += 1
        self.blood_type = blood_type
        self.prioritary = random.choice([True, False, False, False, False]) #i want 20% prioritary humans

        while blood_type != "A" and blood_type != "B" and blood_type != "AB" and blood_type != "O":
            blood_type = input(f"please {self.name} put A,B,AB or O for the blood type: ")
            self.blood_type = blood_type
                
    def __repr__(self):
        return f"Name {self.name}, age {self.age}, id {self.id_number} prioritary {self.prioritary} "

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


    def all_family_members(self):
        family_members = list(set(self.family))
        return f"All my family members: \n {self.family}"

# 2) Queue
# Represents a queue of humans waiting for their vaccine. It has two attributes, humans,
#  the list containing the humans that are waiting, it is initialized empty.
# This class is useful to manage who will get vaccinated in priority. It has the following methods:

class Queue():

    def __init__(self):

        self.humans_on_list = []

# add_person(self, person) Add a human to the queue,
#  if he is older than 60 years old or a prioritary person, 
# put him at the beginning of the list (at index 0) before every other.


    def addPerson(self, person):
        if person.age < 60 and not person.prioritary:
            self.humans_on_list.append(person)
        else:
            self.humans_on_list.insert(0, person)


# find_in_queue(self, person) Returns the index of a human in the queue.


    def find_in_queue(self, person):
        for human in self.humans_on_list:
            if human.name == person.name:
                return self.humans_on_list.index(person)

# swap(self, person1, person2) Swaps person1 with person2.


    def swap(self, person1, person2):
        person1_index = self.humans_on_list.index(person1)
        person2_index = self.humans_on_list.index(person2)
        self.humans_on_list.remove(person1)
        self.humans_on_list.remove(person2)
        self.humans_on_list.insert(person1_index, person2)
        self.humans_on_list.insert(person2_index, person1)

# get_next(self) return the next human in the queue, meaning the object at index 0 in the list.


    def getNext(self):
        if len(self.humans_on_list) > 0:
            human_to_get_vaccinate = self.humans_on_list[0]
            self.humans_on_list.pop(0)
            return human_to_get_vaccinate
        else:
            return None


# get_next_blood_type(self, blood_type) Return the first human with this specific blood type.

    def get_next_blood_type(self, blood):
        for human in self.humans_on_list:
            if human.blood_type == blood:
                human_with_blod_type_to_get_vaccinate = human
                self.humans_on_list.remove(human)
                return human_with_blod_type_to_get_vaccinate
        return None

# sort_by_age(self) Sort the queue so that the older ones are before the younger ones 
# and all the prioritary persons are before the others.
# Every human returned by get_next and get_next_blood_type is removed from the list, 
# those functions return None if there is no one in the list.


    def sort_by_age_and_prioritary(self):
        for i in range(len(self.humans_on_list)):
            for i in range(len(self.humans_on_list)- 1):
                    person1 = self.humans_on_list[i]
                    person2 = self.humans_on_list[i + 1]
                    
                    if person1.prioritary and person2.prioritary:
                        if person1.age < person2.age:
                            self.swap(person1, person2)
                        else:
                            continue
                    elif person1.prioritary and not person2.prioritary:
                        continue
                    elif not person1.prioritary and person2.prioritary:
                        self.swap(person1, person2)
                    elif not person1.prioritary and not person2.prioritary:
                        if person1.age < person2.age:
                            self.swap(person1, person2)
                        else:
                            continue
        return self.humans_on_list


    def rearange_queue(self):
        for i in range(3):
            for i in range(len(self.humans_on_list)- 2):
                    person1 = self.humans_on_list[i]
                    person2 = self.humans_on_list[i + 1]
                    if person1 in person2.family:
                        self.humans_on_list.remove(person2)
                        self.humans_on_list.insert(i + 2, person2)
                    else:
                        continue
        return self.humans_on_list



# Part 2
# Create an attribute family for the Human class. Initialized as empty, family is a list of all 
# the humans that are living in the same house with this human. Add a method add_family_member(self, person)
#  that adds the person to this human’s family and this human to the person’s family.

# Add the rearange_queue(self) method to the Queue class, so that there is no two members of the same family one after the other.




alisa = Human("alisa", 27, "B")

gaston = Human("gaston", 32, "O")

mario = Human("mario", 78, "AB")

isaac = Human("Isaac", 45, "A")

peter = Human("peter", 88, "AB")

laura = Human("laura", 15, "B")

anonimo77 = Human("no name", 12, "O")

diego = Human("diego korn", 55, "O")



# vacunados_israel_2021 = Queue()

# vacunados_israel_2021.addPerson(alisa)
# vacunados_israel_2021.addPerson(gaston)
# vacunados_israel_2021.addPerson(isaac)
# vacunados_israel_2021.addPerson(mario)
# vacunados_israel_2021.addPerson(diego)
# vacunados_israel_2021.addPerson(laura)
# vacunados_israel_2021.addPerson(anonimo77)
# vacunados_israel_2021.addPerson(peter)

# vacunados_israel_2021.swap(alisa, gaston)
# print(vacunados_israel_2021.humans_on_list)
# print(vacunados_israel_2021.getNext())
# print(vacunados_israel_2021.get_next_blood_type("O"))
# # print(alisa.blood_type)
# print(vacunados_israel_2021.sort_by_age_and_prioritary())
# alisa.add_family_member(gaston)
# alisa.add_family_member(mario)
# alisa.add_family_member(diego)
# gaston.add_family_member(diego)
# anonimo77.add_family_member(peter)

# print(alisa.all_family_members())
# print(diego.all_family_members())
# print(vacunados_israel_2021.rearange_queue())