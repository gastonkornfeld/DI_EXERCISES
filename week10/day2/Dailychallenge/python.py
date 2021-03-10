
from translate import Translator
# Daily Challenge :
# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.




translator = Translator(to_lang = "fr")
translation = translator.translate("hello my friend how are you")
print(translation)


french_words = {}

def add_translated_french_words(dictionary_to_make):
    word_to_translate = ""
    translator = Translator(to_lang = "fr")
    while word_to_translate != "exit":
        print("write exit when you finish")
        word_to_translate = input("write an english word to translate an put in the dictionary: \n")
        print(word_to_translate)
        word_translation = translator.translate(word_to_translate)
        print(word_translation)
        dictionary_to_make[word_to_translate] = word_translation
    return dictionary_to_make

print(add_translated_french_words(french_words))




