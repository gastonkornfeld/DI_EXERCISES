



# Download my_text.txt

# Write a class called Text, it accepts a string as argument and store the text in a attribute.
# Implement the following:

# a classmethod that returns a instance of Text but with a text file: >>> Text.from_file('my_text.txt')


class Text():
    

    def __init__(self, book_title):
        self.book_title = book_title
        text_file_name = "the_stranger.txt"
        try:
            with open(text_file_name, mode='r') as book:
                self.book_lines = book.readlines()
                book.seek(0)
                self.book_complete_text = book.read()
        except:
            print("the files doesnt exist")

    @classmethod
    def from_file(cls, title):
        try:
            with open(title, mode='r') as book:
                book_text_from_file = book.read()
        except:
            print("the file doesnt exist")

        return book_text_from_file

# a method to return the frequency of a word in the text (assume words are separated by whitespace)
#  return None or meaningful message

    def word_count(self, word_to_find):
        counts = 0
        words = self.book_lines
        for line in words: # iterate the lines of the book
            list1 = line.split()  # list of the words in each line
            for word in list1:
                if word == word_to_find:
                    counts += 1
                else:
                    continue
        if counts == 0:
            return None
        else:
            return f"The word '{word_to_find}' appears in this book {counts} times!!!!"



# print(book1.word_count("dog"))

# a method that returns the most common word in the text


    def mostCommonWord(self):
     
        counts = dict()
        words = self.book_lines
        for line in words: # iterate the lines of the book
            list1 = line.split()  # list of the words in each line
            for word in list1: #chek every word
                word1 = word.lower()
                if word1 in counts: #if is already in the dic
                    counts[word1] += 1 
                else:
                    counts[word1] = 1
        # lets look for the max number
        list_of_ammount = []
        for words_in_dic in counts: # append all the ammounts in to a list to chek the max of the list
            list_of_ammount.append(counts[words_in_dic])
        max_ammount = max(list_of_ammount)
        # now knowing the max i search in the list wit that number
        # because can be more than one word having the max i will append to a list
        list_of_words_with_max_ocurrence = []
        for words_in_dic in counts:
            if counts[words_in_dic] == max_ammount:
                list_of_words_with_max_ocurrence.append(words_in_dic)
        return f"The word\s with more appereance : {list_of_words_with_max_ocurrence} with {max_ammount} times"

# a method that returns a list of the unique words in the text

    def uniqueWords(self):
     
        counts = dict()
        words = self.book_lines
        for line in words: # iterate the lines of the book
            list1 = line.split()  # list of the words in each line
            for word in list1: #chek every word
                word1 = word.lower()
                if word1 in counts: #if is already in the dic
                    counts[word1] += 1 
                else:
                    counts[word1] = 1
        

        ammount = 1
        # because can be more than one word having only one appearence I use a list
        list_of_words_with_unique_ocurrence = []
        for words_in_dic in counts:
            if counts[words_in_dic] == ammount:
                list_of_words_with_unique_ocurrence.append(words_in_dic)
        return f"The word\s with unique appereance : {list_of_words_with_unique_ocurrence}"









 

# Write a TextModification class that inherits from Text

class TextModification(Text):
    
    # a method that returns the text without punctuation
    def withoutPunctuation(self):
        punctuations = '''!-;:'",._'''
        words = self.book_complete_text
        new_text = ""
        for char in words:
            if char not in punctuations:
                new_text += char
        print(new_text)

# a method that returns the text without english stop-words (check out what this is !!)            
    def withoutEnglishStopWords(self):
        stop_words = Text.from_file("stop_words.txt")
        list_of_stop_words = stop_words.split()
        words = self.book_lines
        book_without_stop_words = ""
        for line in words: # iterate the lines of the book
            list1 = line.split()  # list of the words in each line
            for word in list1:
                if word not in list_of_stop_words:
                    book_without_stop_words += word + " "
        print(book_without_stop_words)
        
        
# a method that returns the text without special characters
    def withoutSpecialCharacters(self):
        punctuations = '''()-[]{}\<>/@#$%^&*~`+=|'''
        words = self.book_complete_text
        new_text = ""
        for char in words:
            if char not in punctuations:
                new_text += char
        print(new_text)



# Now, use the provided txt file and try using the class you created above.
# Note: Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

# book1 = Text("the_stranger.txt")
# count1 = book1.word_count('lion')
# print(book1.mostCommonWord())
# print(book1.uniqueWords())
# print(Text.from_file("the_stranger.txt"))

text1 = TextModification("hola")
print(text1.withoutPunctuation())
# text1.withoutEnglishStopWords()
# text1.withoutSpecialCharacters()


