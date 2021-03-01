



# Exercise 1 : Pets
# Consider this code

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Fluffy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

    def walk(self):
        return f'{self.name} is just a fluffy cat walking around'

bengal_cat_1 = Bengal("murdock", 3)
chartreux_cat_1 = Chartreux("tom", 2)
fluffy_cat_1 = Fluffy("kelly", 1)

my_cats= [bengal_cat_1, chartreux_cat_1, fluffy_cat_1]

My_pets_in_2021 = Pets(my_cats)
My_pets_in_2021.walk()


# Add another cat breed
# Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# Instantiate the Pet class with all your cats. Use the variable my_pets
# Output all of the cats walking using the my_pets instance











# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, 
# returns string of which dog won the fight between them, whichever has a higher run_speed x weight should win.
# Create 3 dogs and use some of your methods



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
        self.speed = (self.weight/self.age) * 10
        print(f'{self.name} speed is {self.speed}')


    def fight(self, other):
        print(f"{self.name} is fighting {other.name}")
        if self.power > other.power:
            print(f"{self.name} won the battle with {self.power} power. the losing dog is {other.name} with {other.power} power")
        else:
            print(f"{other.name} won the battle with {other.power} power. the losing dog is {self.name} with {self.power} power")



dog1 = Dog("tom", 3, 60)
dog2 = Dog("marcos", 4, 70)
dog3 = Dog("aquiles", 1, 70)


dog1.run_speed()
dog2.run_speed()
dog3.run_speed()
dog1.fight(dog2)
dog2.fight(dog3)


a = input("")



