
import random



# Exercise : Double Dice
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

def throw_dice():
    dice = random.randint(1, 6)
    return dice

# print(throw_dice())

def throw_until_doubles():
    dice1 = 1
    dice2 = 2
    count_dices = 0
    while dice1 != dice2:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count_dices += 1
    return count_dices

# print(throw_until_doubles())


# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you to decide on what data structure to use).

def main():
    all_results = []
    for i in range (100):
        how_many_dices = throw_until_doubles()
        all_results.append(how_many_dices)
    return all_results

game = main()
# print(main())

# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
print(f"Took {sum(game)} throws in total to reach 100 doubles")


# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:
print(f"Average throws to reach doubles: {float(sum(game)/100)}")

# If the results of the throws were as follows (your code would do 100 doubles, not just 3):

# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)
# Then my output would show something like this:

# Total throws: 8
# Average throws to reach doubles: 2.67.
