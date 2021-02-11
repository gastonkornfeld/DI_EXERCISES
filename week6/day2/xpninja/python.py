




# my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum.'''

# lenght_of_my_text = len(my_text)
# print(lenght_of_my_text)







# Exercise 5: Longest Word Without A Specific Character
# Keep asking the user to input the longest sentence they can without the character “A” in it
# Each time a user successfully sets the new longest sentence print a congratulations message



user_sentence = input("tell me allways a longer sentence without 'a' on it: ")
leng_of_the_sentence = len(user_sentence)
last_sentence_lenght = 0  

while last_sentence_lenght < leng_of_the_sentence:
    if "a" in user_sentence:
        print("You use 'a', Game over")
        break
    last_sentence_lenght = len(user_sentence)
    print("Congratulations")
    user_sentence = input("New longer Sentence: ")
    leng_of_the_sentence = len(user_sentence)
     
print("end of the game")



