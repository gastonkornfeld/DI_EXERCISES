
    
 
class Human:

    def __init__(self, name, age, color_of_eyes, speed):
        self.name = name
        self.age = age
        self.eye_color = color_of_eyes
        self.speed = speed
        self.passengger_of = None
    def introduce(self):
        print(f"{self.name} has {self.eye_color} eyes and is {self.age} years old")

    def set_eye_color(self, new_color):
        self.eye_color = new_color

    def birthday(self):
        """
        Prints a happy birthday message and increments the age by 1
        :return:
        """
        print(f"Happy birthday {self.name} !")
        self.age += 1

    def run(self, distance):
        """
        Return the time that it takes to this human to run this distance
        (reminder time = distance/speed)
        :param distance: distance in km
        :return:
        """
        return distance/self.speed

    def say_hello(self, other):
        """
        Say hello to another human
        :param other: (Human) the human to say hello to
        """
        print(f"{self.name} says hello to {other.name}")

    def is_older(self, other):
        """
        Checks if this human is older than the other
        It should print someething like:
            "Bill (42) is older than matt (22)"
        :param other: (Human)
        :return:
        """
  


        if self.age > other.age:
            # Self is older
            print(f"{self.name} ({self.age}) is older than {other.name} ({other.age})")

        elif other.age > self.age:
            # The other is older
            print(f"{other.name} ({other.age}) is older than {self.name} ({self.age})")

        else:
            print(f"{self.name} and {other.name} are both {self.age}")

    def car_information(self):
        print(self.passengger_of)


    def race(self, other, distance):
        """
        Make a race between two humans
        It should print something like:
            "Bill arrived first (in 6 seconds), Matt arrived after 8 seconds"
        :param other:
        :param distance: distance to run
        :return:
        """

        self_time = self.run(distance)
        other_time = other.run(distance)

        if self_time < other_time:
            print(f"{self.name} arrived first ({self_time} seconds), {other.name} arrived after {other_time} seconds")
        elif other_time < self_time:
            print(f"{other.name} arrived first ({other_time} seconds), {self.name} arrived after {self_time} seconds")
        else:
            print(f"{self.name} and {other.name} both arrived in {self_time} seconds")

class Car:

    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.passengers = []
        self.travelled_km = 0


    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        passenger.passengger_of = self


    def print_info(self):
        print(f"This {self.color} {self.manufacturer} travelled {self.travelled_km} km")

    def travel(self, distance):
        # Print we're travelling
        print(f"The car is travelling {distance} km")

        # Adding the distance to current kilometers of the car
        self.travelled_km += distance       




bill = Human("Bill", 17, "blue", 20)
bill_car = Car("blue" ,"bus")

bill_car.add_passenger(bill)
print(bill_car)


bill.car_information()






class Fruit():
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        self.is_contained = None
class Cart():

    def __init__(self, size):
        self.size = size
        self.content = []

    def addFruit(self, fruit_name):
        if len(self.content) < self.size:
            self.content.append(fruit_name)
            print(f"basket content now is {self.content} kilograms")
            fruit_name.is_contained = self
        return self.content

apple = Fruit(2, 3.5)
cart1 = Cart(10)

print(cart1.addFruit(apple))


















class Animal():
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping  now")


class Cat(Animal):

    def __init__(self, name):
        self.name = name



class Dog(Animal):

    def __init__(self,name):
        self.name= name


    def bark(self):
        print(f"{self.name} says wofff")


cat1 = Cat("pepito")
fluffy = Cat("Fluffy")


fluffy.eat()

cat1.sleep()
cat1.eat()

dog1 = Dog("gato")
dog1.bark()







class Telephone():

    def __init__(self, phone_number, price):
        self.phone_number = phone_number
        self.price = price

    def call(self, number):
        print(f"{self.phone_number} is calling {number}")




class Smartphone(Telephone):

    

    def send_message(self, number, content):
        print(f" The message: \n\n {content} \n \n was succefully sended to the number {number}")



my_phone = Smartphone("0555444555", 33)
my_phone.send_message("873642874632", "hello i was missing you when we can see each other")



