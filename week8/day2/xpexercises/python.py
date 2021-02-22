



# Exercise 1: Cats
# Consider this class

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest_cat(self, other1, other2):
        if self.age > other1.age and self.age > other2.age:
            print(f"The oldest cat is {self.name} , and is {self.age} years old.")
        elif other1.age > self.age and other1.age > other2.age:
            print(f"The oldest cat is {other1.name} , and is {other1.age} years old.")
        else:
            print(f"The oldest cat is {other2.name} , and is {other2.age} years old.")



# Instantiate 3 Cat objects using our class
# Create a function that finds the oldest cat and returns the cat
# Print out: “The oldest cat is , and is years old.” using the method previously created


cat_tom = Cat("tom", 4.5)
cat_tim = Cat("tim", 2.5)
cat_mellower = Cat("mellower", 1.5)

cat_tom.oldest_cat(cat_tim,cat_mellower)
cat_tim.oldest_cat(cat_tom,cat_mellower)







# Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : 
# nameand height. This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog():

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2}cm high!!")

dog_1 = Dog("peter", 45)

dog_1.bark()
dog_1.jump()

davids_dog = Dog("Rex", 50)
davids_dog.jump()
davids_dog.bark()


sarah_dog = Dog("Teacup", 20)
sarah_dog.jump()
sarah_dog.bark()

if davids_dog.height > sarah_dog.height:
    print(f" {davids_dog.name} is taller with {davids_dog.height}cm")
else:
    print(f" {sarah_dog.name} is taller with {sarah_dog.height}cm")










# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

lyrics1 = ["El dia que me quieras", "la flor de un nuevo dia", "se vestira de fiesta", "con su mejor color"]
class Song():

    def __init__(self, name , list_of_lyrics):
        self.list_of_lyrics = list_of_lyrics
        self.name = name

    def sing_me_a_song(self):
        print(f"The title of the song is {self.name}")
        for line in self.list_of_lyrics:
            print(line)

song1 = Song("balada", lyrics1)

song1.sing_me_a_song()











# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = ["crocodile", "panda", "bear", "bufallo", "penguin"]

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"the {new_animal} was added")
        else:
            print(f"you already have {new_animal} in your zoo")

    def get_animal(self):
        print(self.animals)

    def animal_sold(self, animal_sold):
        if animal_sold not in self.animals:
            print(f"you dont have {animal_sold} cant sell them")
        else:
            print(f"{animal_sold} was sold")
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_list = sorted(self.animals)
        final_list = {}
        index_of_the_letter = 0
        parcial_list = []
        for item in range(len(self.animals)-1):
            first = sorted_list[item][0:1]
            second = sorted_list[item+1][0:1]
            if first == second:
                parcial_list.append(sorted_list[item])
            else:
                parcial_list.append(sorted_list[item])
                final_list[index_of_the_letter] = parcial_list
                parcial_list = []
                index_of_the_letter += 1
        for item in final_list:
            print(f"group {item}")
            print(final_list[item])

                
                

# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }

ramat_gan_safari = Zoo("ramat gan zafari")
ramat_gan_safari.add_animal("lion")
ramat_gan_safari.add_animal("giraffe")
ramat_gan_safari.add_animal("giraffe")

ramat_gan_safari.get_animal()
ramat_gan_safari.animal_sold("fish")
ramat_gan_safari.animal_sold("lion")
ramat_gan_safari.get_animal()

ramat_gan_safari.sort_animals()



# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example

# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)





