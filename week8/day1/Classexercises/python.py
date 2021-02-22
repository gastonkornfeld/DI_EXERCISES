


start_position = 0
class Bike():

    def __init__(self, start_position, color, max_speed):
        print("a new bike was made")
        self.start_position = start_position
        self.color = color
        self.max_speed = max_speed
        print(f'the bike color {color} starts at position {start_position}')
        print(f"Max speed {max_speed}")


    def goForward(self, meters):
        print(f"the bike moves {meters} meters forward")
        actual = self.start_position
        print(f"actual position : {actual}")

    def movePosition(self, position):
        return f"the bike is in position {position}"
     

    
    
        


bike_number_1 = Bike(1, "red", 123)
bike_number_2 = Bike(2, "blue", 111)



print(bike_number_2)
print(bike_number_1.goForward(100))
print(bike_number_1.goForward(100))
print(bike_number_1.start_position)






class Human():
    def __init__(self, name, age, eye_color, speed):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.speed = speed

    def introduce(self):
        return f"hello i am {self.name} I am {self.age} years old and have {self.eye_color} eyes. \n My speed is: {self.speed}km/h"

    def happy_birthday(self):
        self.age += 1
        return(f"Happy Birthday {self.name} now you have {self.age} years old")

    def retired(self):
        if self.age > 65:
            return True
        else:
            return False

    def how_much_take_to_run_this_distance(self, distance):
        time = distance/self.speed
        return f"{self.name} take {time} hours to run {distance}km"

    def say_hello(self, other):
        return f"{self.name} says hello to {other.name}"


    def is_older(self, other):
        if self.age > other.age:
            return f"{self.name} is older than {other.name}"
        else:
            return f"{other.name} is older than {self.name}"



    
matt = Human("matt", 33, "green", 7)
lisa = Human("lisa", 22, "brown", 5)

print(matt.introduce())
print(lisa.introduce())
print(lisa.happy_birthday())
print(matt.retired())
print(matt.is_older(lisa))


print(matt.how_much_take_to_run_this_distance(100))

print(matt.say_hello(lisa))