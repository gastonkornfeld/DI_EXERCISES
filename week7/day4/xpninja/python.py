



# Exercise 1 : What’s Your Name ?
# Write a function called get_full_name() that receives three arguments: a first_name, a middle_name and a last_name.
# But the middle_name should be optional, if it’s omitted by the user, the name returned will only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.



# def get_full_name(first_name, last_name,  middle_name = "" ):
#     return f"{first_name} {middle_name} {last_name}"



# print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))

# print(get_full_name(first_name="bruce", last_name="lee"))












# Exercise 2 : From English To Morse
# Write a function that converts English text to Morse code and another one that does the opposite.
# Hint: Check on internet for translation table, every letter is separated with a space and every word is separated with a slash /.



# english_morse_dictionary = {
#     "a": ".- ", 
#     "b":  "-... ", 
#     "c": "-.-. ", 
#     "d": "-.. ",
#     "e": ". ",
#     "f": "..-. ",
#     "g": "--. ", 
#     "h": ".... ",
#     "i": ".. ",
#     "j": ".--- ",
#     "k": "-.- ",
#     "l": ".-.. ",
#     "m": "-- ",
#     "n": "-. ",
#     "o": "--- ",
#     "p": ".--. ",
#     "q": "--.- ",
#     "r": ".-. ",
#     "s": "... ",
#     "t": "- ",
#     "u": "..- ",
#     "v": "...- ",
#     "w": ".-- ",
#     "x": "-..- ",
#     "y": "-.-- ",
#     "z": "--.. ",
#     " ": "/ "


# }

# phrase_to_translate = input("what do yo want to translate to morse code: ")


# def from_english_to_morse(phrase):
#     morse_messagge = ""
#     for letter in phrase:
#         morse_messagge += english_morse_dictionary[letter]
#     return morse_messagge


# print(from_english_to_morse(phrase_to_translate))



morse_english_dictionary = {
    ".- ": "a", 
    "-... ": "b", 
    "-.-. ": "c", 
    "-.. ": "d",
    ". ": "e",
    "..-. ": "f",
    "--. ": "g", 
    ".... ": "h",
    ".. ": "i",
    ".--- ": "j",
    "-.- ": "k",
    ".-.. ": "l",
    "-- ": "m",
    "-. ": "n",
    "--- ": "o",
    ".--. ": "p",
    "--.- ": "q",
    ".-. ": "r",
    "... ": "s",
    "- ": "t",
    "..- ": "u",
    "...- ": "v",
    ".-- ": "w",
    "-..- ": "x",
    "-.-- ": "y",
    "--.. ": "z",
    "/ ": " ",
}

def from_morse_to_english(phrase):
    english_messagge = ""
    parcial_value= ""
    for morse_letter in phrase:
        parcial_value += morse_letter
        
        if parcial_value in morse_english_dictionary:
            english_messagge += morse_english_dictionary[parcial_value]
            parcial_value = ""
    return english_messagge
        
       


test_morse_code = ".... --- .-.. .- / .. -. ... - .-. ..- -.-. - --- .-. / -.. . / .--. -.-- - .... --- -. "

print(from_morse_to_english(test_morse_code))

