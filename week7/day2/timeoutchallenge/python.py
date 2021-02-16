


# Count Occurence
# Write a program which takes as input a string and a character, and finds out the number of occurrences of the given character in the string.

# String: Programming is cool!
# Character: o
# 3
# String: This is a great example
# Character: y
# 0
phrase_given= input("give me a phrase")
string_to_look = input("wich character you want to count inside the phrase?")

def count_occurence(phrase, character):
    
    how_many = phrase.count(character)
    return f"The character {character} is {how_many} times in the phrase you ask for"


print(count_occurence(phrase_given, string_to_look))