# Anagram Checker
# We will create a program that will ask the user for a word. It will check if the word is a valid English word, and then find all possible anagrams for that word.



# First Download this text file



# In a new file called anagram_checker.py, create a class called AnagramChecker
# The class should have the following methods:



class anagramChecker():
    invalid_characters = '''()-[]{}\<>/@#$%^&*~`+=|!-;:'",._0123456789'''    

# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on.


    def __init__(self):
        self.list_of_words_for_anagram = getWords()

# is_valid_word(word) – should check if the given word (‘word’) is a valid word.



    def is_valid_word(self, word):
        for char in word:
            if char not in anagramChecker.invalid_characters:
                # print(char)
                continue
            else:
                return False
        word1 = word
        list10 = word1.split()
        if len(list10) > 1:
            return False
        else:
            return True



# (Hint: you might want to create a separate method called is_anagram(word1, word2), 
# that will compare 2 words and return True if they contain exactly the same letters 
# (but not in the exact same order), and False if not.)
    @staticmethod
    def is_anagram(word1, word2):
        word1_count = {}
        word2_count = {}
        word1 = word1.lower()
        word2 = word2.lower()
        for char in word1:
            if char in word1_count:
                word1_count[char] += 1
            else:
                word1_count[char] = 1
        for char2 in word2:
            if char2 in word2_count:
                word2_count[char2] += 1
            else:
                word2_count[char2] = 1
        if word1_count == word2_count:
            return True
        else:
            return False



# get_anagrams(word) – should find all anagrams for the given word. 
# (eg. if ‘word’ is ‘meat’,the function should return a list containing [‘mate’, ‘tame’, ‘team’].)
# Note: None of the methods of this class should print anything to output.




    def get_anagrams(self, word_to_get_anagrams):
        list_to_chek = self.list_of_words_for_anagram
        new_list = []
        for word in list_to_chek:
            word_1 = word[0:-2].lower()
            new_list.append(word_1)
        # print(new_list)
        

        anagrams_of_the_word = []
        for word3 in new_list:
            
            # print(word3)
            if anagramChecker.is_anagram(word3, word_to_get_anagrams):
                # print(word3)
                anagrams_of_the_word.append(word3)
        anagrams_of_the_word = list(set(anagrams_of_the_word))        
        return anagrams_of_the_word










def getWords():
    file_with_all_the_words = "sowpods.txt"
    try :
        with open(file_with_all_the_words, mode='r') as anagram_words:
            all_the_words = anagram_words.readlines()
            return all_the_words      
    except:
        print("the files doesnt exist")






anagram = anagramChecker()
anagram.get_anagrams("cheat")
# print(anagram.is_valid_word("gato"))
