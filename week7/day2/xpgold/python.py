import random


# Exercise 1: Temperature Advice
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.




# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’. Make sure to display a meaningful prompt.
# Use the season as an argument when calling get_random_temp().

# Bonus: give the temperature as a floating-point number instead of an integer
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month (this page may help you).)


def get_random_temp(season):
    
    if 3 < season < 7:
        return random.uniform(23, 45)
    elif 0 < season < 4:
        return random.uniform(18, 36)
    elif 6 < season < 10:
        return random.uniform(12, 33)
    elif 9 < season < 13:
        return random.uniform(-20, 12)

    
    









# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature, together with a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Add more functionality to the main() function, writing some friendly advice relating to the temperature, if it is:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

in_wich_month_we_are = int(input("Put the number of the month we are, ex for december: 12 \n"))


def main():
    
    temperature = get_random_temp(in_wich_month_we_are)
    print(f"The temperature right now is {temperature} degrees celsius")
    if temperature <= -10:
        return f"BRRRRR That is a really really really cold day there"
    elif -10 < temperature < 0:
        return f"BRRRRR That is a really  cold day outside"
    elif 0 < temperature < 16:
        return f"better to put a nice coat is cold outside"
    elif 16 <= temperature < 23:
        return f"You will need a sweater it is chill outside"
    elif 23 <= temperature < 32:
        return f"It is nice outside, just carry a sweater for the night"
    elif 32 <= temperature < 45:
        return f"Such a hot day today outside"


    



print(main())




