import random


# Exercise 1
# Create a Door class, it has only the following attributes:

# id (int) An id number, use a class variable objs that counts 
# how many door have been created so far and use this number as the id of the door.
# locked (boolean)


class Door():
    '''
        Create a door that have id= number of doors created, starting from 0
        The door is going to be locked or not in a relation of 1:2
    '''
    doorsCreated = 0
    listOfDoors = []
    NumberOfKeys = 5
    def __init__(self):
        
        self.id = Door.doorsCreated
        Door.doorsCreated += 1
        self.locked = random.choice([False, False, True, False, True])
        Door.listOfDoors.append(self)
    
    def __repr__(self):
        return f"Door id {self.id} Locked:{self.locked}"

    
    def next(self):
        index = 0
        for door in Door.listOfDoors:
            if door.id == self.id:
                index_of_the_door = index
                print(f"Actual door {Door.listOfDoors[index]} Next door : {Door.listOfDoors[index + 1]}")
            else:
                index += 1
        return Door.listOfDoors[index_of_the_door + 1]


    def random(self):
        randomDoor = random.choice(Door.listOfDoors)
        print(f"next door {randomDoor}")
        return randomDoor

    def canGoTo(self, other):
        if not other.locked:
            print("you got throw the door")
            return True
        return False
        
    def display(self):
        
        while Door.NumberOfKeys != 0:
            print(f"you are in {self}")
            this_door = self
            next_door = self.next()
            
            can_go = this_door.canGoTo(next_door)
            if can_go:
                self = next_door
            else:
                print(f"you need a key to open the door, \n door open... \n")
                Door.NumberOfKeys -= 1
                next_door.locked = False
                print(f"{Door.NumberOfKeys} keys left")




# next (List of Door obs) The next doors available from this one
# Create a method can_go_to(self, other_door) in the Door class that 
# checks if the path from this door to other_door can be made (the locked doors cannot be opened !).

# Bonus: Display the path
# Bonus 2: Add an integer variable KEYS that holds a limited number of keys
#  available to open locked doors (each key can be used only once).




door1 = Door()
door2 = Door()
door3 = Door()
door4 = Door()
door5 = Door()
door6 = Door()
door7 = Door()
door8 = Door()
door9 = Door()
door10 = Door()
door11 = Door()
door12 = Door()
# print(door4.id)
door13 = Door()
door14 = Door()
door15 = Door()
door16 = Door()
door17= Door()
door18 = Door()
door19= Door()
door20 = Door()
door21 = Door()
door22 = Door()
door23 = Door()
door24 = Door()
door25 = Door()

# print(door4)

# print(door1.next())
# door1.canGoTo(door2)

door1.display()