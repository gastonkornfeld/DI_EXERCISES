
# hang man game


word_to_guess = ""

while len(word_to_guess) < 8:
    word_to_guess = input("put the word you want to be guess, 8 letters minimum: \n")


# first i will put the word in to a list and also a list of * with the same lenght

word_in_a_list = []

for letter in word_to_guess:
    word_in_a_list.append(letter)

list_with_secret_word = []

for letter in word_to_guess:
    list_with_secret_word.append("*")
wordinasterisc = " ".join(list_with_secret_word)
print(f"This is the word to guess: {wordinasterisc}")


# now i should ask the user for a letter
# also i start an error backwards counter and a list of the word the user already said
mistakes = 10 
list_of_letters_already_sayd = []
user_letter_guess = ""
while word_in_a_list != list_with_secret_word:
    # ask the user for a letter
    user_letter_guess = input("tell me a letter you think is in the word: ")
    # check if the letter the user say he already say it and tell the user
    if user_letter_guess in list_of_letters_already_sayd:
        print("you already say this letter")
        print(f"this is the list of letters you already said: \n {list_of_letters_already_sayd}")
        continue
    list_of_letters_already_sayd.append(user_letter_guess)
    if user_letter_guess in word_in_a_list:
        for i in range(len(word_in_a_list)):
            # im looping for the list to change all the coincidences
            if word_in_a_list[i] == user_letter_guess:
                list_with_secret_word[i] = user_letter_guess
                word = " ".join(list_with_secret_word)
        print(f"perfect {user_letter_guess} it was in the word")
        print(f"the actual word is now: {word}")
    else:
        mistakes = mistakes - 1
        print(f" the letter '{user_letter_guess}' is not in the word, you have {mistakes} mistakes left")
        word = " ".join(list_with_secret_word)
        print(word)
        if mistakes == 0:
            print("you are out of mistakes you lose")
            break
    print("Amazing you won")





