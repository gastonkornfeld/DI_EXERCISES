
import random



# Exercise 1 : What Are You Learning ?
# Write a function called display_message() 
# that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.



def display_message(learning):
    
    return f"This week we are learning {learning}"

print(display_message("Functions"))










# Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.




def favorite_book(title):
    
    return f"One of my favourites books is: {title}"

print(favorite_book("Alice in wonderland"))














# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.




def describe_city(city, country="Argentina"):
    return f"{city} is in {country}"

print(describe_city("cordoba"))
print(describe_city("sevilla", "Espana"))
print(describe_city("Malaga"))












# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 
# and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display
#  a success message to the user, otherwise show a fail message and display both numbers



def random_and_random(number):
    number2 = random.randint(0,100)
    if number == number2:
        return f"asewome, the two numbers are equal"
    else:
        return f"not lucky {number} is not equal to {number2}"


print(random_and_random(27))






# Exercise 5 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



def make_shirt(size="L", message="I love python"):
    return f"We need to print a shirt size: {size}, with the message: '{message}'"

print(make_shirt("XXL", "I Am looping in python"))
print(make_shirt(size="XS", message= "Peace"))
print(make_shirt(size="M"))
print(make_shirt())
print(make_shirt(size="XXS", message= "Peace all around the world"))







# Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.



magicians = ["Merlin", "gaspar", "Radagast", "Mercury", "Iron man"]

def show_magicians(list_of_names):
    for name in list_of_names:
        print(name)
    

print(show_magicians(magicians))


def make_great(list_of_names):
    for name in list_of_names:
        name = name + " the great"
        print(name)



print(make_great(magicians))
print(show_magicians(magicians)) # did not modify the list


