
from anagram_functions import anagramChecker
import anagram_functions as af

anagram1 = anagramChecker()

# print(anagram1.is_anagram("caca", "cala"))



# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
# It should do the following:
valid_word = False

while True:
    print("welcome to the anagrams program \n")
    # print("write (anagram) to find all the anagrams of a word, you must write only one word, only letters.\n")
    # print('write exit to finish the program \n')
    menu_variable = input("So tell me wath you want to do (anagram) or (exit):  \n")
    if menu_variable == "exit":
        break
    elif menu_variable == "anagram":
        valid_word = False
        while not valid_word:
            word_to_work_with = input("wich word we should find: \n")
            word_to_work_with = word_to_work_with.strip()
            # print(word_to_work_with)
            check_if_valid = anagram1.is_valid_word(word_to_work_with)
            # print(check_if_valid)
            new_list = []
            for word in anagram1.list_of_words_for_anagram:
                word1 = word[0:-2].lower()
                new_list.append(word1)
            # print(new_list)    
            if check_if_valid and word_to_work_with in new_list :
                valid_word = True
                list_of_anagrams = anagram1.get_anagrams(word_to_work_with)
                print(f"{word_to_work_with} is a valid English word")
                print(f"This are the anagrams for the word {word_to_work_with}: {list_of_anagrams}")
                
            else:
                print("please input an English valid word\n")
    else:
        print("only options possible are (anagram) or (exit)\n")

# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.
# Once your code has decided that the user’s input is validated, it should find out:
# if the user’s word is a valid English word, and all possible anagram words for the user’s word.
# The above steps should be done by an instance of the AnagramChecker class.
# Display the information about the word to the user in a user-friendly, nicely-formatted message on the screen. Something like this:

# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.