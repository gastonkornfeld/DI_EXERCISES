my_age = 32
my_age_in_123879_years = my_age + 123879
print("my age in 123879 years will be", my_age_in_123879_years)

first_name = "gaston"
last_name = "Kornfeld"
print("my name is " + first_name + last_name)

# store the amount of cars in a variable
cars = 100
#store the space of each car in a variable
space_in_a_car = 4.0
#store the amount of drivers in a variable
drivers = 30
#store how manny passengers are in a variable
passengers = 90
#calculate the amount of cars without driver
cars_not_driven = cars - drivers
#store the amount of cars with drivers in a variable
cars_driven = drivers
#calculate the amount of passengers you can carry
carpool_capacity = cars_driven * space_in_a_car
#calculate the amount of passengers for car
average_passengers_per_car = passengers / cars_driven
#print the amount of cars avaiable
print("There are", cars, "cars available.")
#print the amount of drivers
print("There are only", drivers, "drivers available.")
#print how many cars still need a driver
print("There will be", cars_not_driven, "empty cars today.")
#print how much passengers the company is able to carry today
print("We can transport", carpool_capacity, "people today.")
#print the amount of passengers of the day using the service
print("We have", passengers, "to carpool today.")
#print the amount of passengers for car needed to fit the requirements of the day
print("We need to put about", average_passengers_per_car,"in each car.")

# i guess is gonna display the age that im gonna be ask for tu put in console inside the frase in the {}.

age = input("How old are you? ")
print("You are {} years old".format(age))



# Write a program that prints the numbers from 1 to 100 inclusive

# But for multiples of three print “Fizz” instead of the number

# For the multiples of five print “Buzz”.

# For numbers which are multiples of both three and five print “FizzBuzz” instead.

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

