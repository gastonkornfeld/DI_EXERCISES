import random

class Dog():

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.speed = (self.weight/self.age) * 10
        self.power = self.speed * self.weight 
        
    def bark(self):
            print("wof wof wof")

    def run_speed(self):
        print(f'{self.name} speed is {self.speed}')


    def fight(self, other):
        print(f"{self.name} is fighting {other.name}")
        if self.power > other.power:
            print(f"{self.name} won the battle with {self.power} power. the losing dog is {other.name} with {other.power} power")
        else:
            print(f"{other.name} won the battle with {other.power} power. the losing dog is {self.name} with {self.power} power")






# Exercise 3 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
# play: gets parameter of any amount of other dogs (look up args) and prints 
# “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly 
# ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”


class PetDog(Dog):
    trained_dog = False
    list_of_dog_tricks = ["does a barrel roll", "stands on their back legs", "shakes your hand" , "plays dead"]
    def train(self):
        self.bark()
        self.trained_dog = True


    def play(self, *other):
        print("the dogs:\n")
        print(f'{self.name}, ')
        for i in range(len(other)):
            other[i].trained_dog = False
            print(f"{other[i].name}, ")
        print(f"Plays togheter")

    def do_a_trick(self):
        trick_number = random.randint(0,3)
        trick_to_be_done = self.list_of_dog_tricks[trick_number]
        if self.trained_dog:
            print(f" {self.name} {trick_to_be_done}")
        else:
            print("Train your dog to make a trick")
        self.trained_dog = False

pet_dog_1 = PetDog("bartolo", 2, 5)
pet_dog_1.train()
print(pet_dog_1.trained_dog)


dog2 = PetDog("carlos", 1, 25)
dog3 = PetDog("juan", 3, 56)
pet_dog_1.play(dog2, dog3)


pet_dog_1.do_a_trick()
pet_dog_1.train()
pet_dog_1.do_a_trick()



