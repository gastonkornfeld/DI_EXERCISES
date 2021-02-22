







# Daily Challenge : Old MacDonald’s Farm
# Look carefully at this code and output
# File: market.py
# Create the code that is needed to recreate the code above.
#  Here are a few questions to help give you some direction:
# 1. Create a Farm class. How do we implement that?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many method does the Farm class need ?
# 4. Do you notice anything interesting about the way we are calling the add_animal method?
#  What parameters should this function have? How many…?
# 5. Test that your code works and gives the same results as the example above.
# 6. Bonus: line up the text nicely in columns like in the example using string formatting
# Output

class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = {}
        print(f"{self.name}'s farm")


    def add_animal(self, animal, amount=1):
        if animal not in self.animals:
            self.animals[animal] = amount
            
        else:
            amount = self.animals[animal] + amount
            self.animals[animal] = amount


    def get_info(self):
        for animal in self.animals:
            print(f"{animal} : {self.animals[animal]}")
        print()
        return("        E-I-E-I-O!")


    def get_animal_types(self):
        list_of_animal = []
        for animal in self.animals:
            list_of_animal.append(animal)
        list_of_animal_sorted = sorted(list_of_animal)
        return list_of_animal_sorted


    def get_short_info(self):
        list_of_sorted_animals = self.get_animal_types()
        string_to_print = str(self.name) + "'s farms have "
        
        for i in range(len(list_of_sorted_animals)):
            if i == len(list_of_sorted_animals) - 1:
                string_to_print = string_to_print + " and " + list_of_sorted_animals[i] + "s."
            else:
                string_to_print = string_to_print + list_of_sorted_animals[i] + "s, "
            
        print(string_to_print)



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('alisa',255)
macdonald.add_animal('cat', 15)
macdonald.add_animal('duck', 56)
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()



# Expand The Farm
# Add a method to the Farm class called get_animal_types.
#  It should return a sorted list of all the animal types (names) that the farm has in it.
#  For the example above, the list should be: ['cow', 'goat', 'sheep']
# Add another method to the Farm class called get_short_info. 
# It should return a string like this: “McDonald’s farm has cows, goats and sheep.”
# It should call the get_animal_types function.
# How would we make sure each of the animal names printed has a comma after it
#  aside from the one before last (has an and after) and the last(has a period after)?.