
import json
import random

# # Exercise 1 – Random Sentence Generator
# # Description: We will create a program that will generate a random sentence and display it to the user.
# #  We will allow the user to choose how long the sentence will be.

# # Hint : The random sentences do not need to make sense or to be grammatically correct

# # Download this word list

# # Save it in your development directory.

# # Create a function called get_words_from_file that will read the file’s contents and return them as a collection. 
# # What data type should you use?
# file_name1 = "sowpods.txt"
# def getWordsFromFile(file):
#         try:
#             with open(file, mode='r') as file_content:
#                 list_of_lines = file_content.readlines()
#                 return list_of_lines
#         except FileNotFoundError:
#             return "i didnt find the file"

# list_of_lines = getWordsFromFile(file_name1)
# # print(list_of_lines)




# # Create another function called get_random_sentence. It should have a single parameter, length, 
# # which will be used to determine how many words the sentence should have.
# #  The function should get the words list, 
# # and choose random words from it, according to the amount specified by length.

# def get_random_sentence(lenght):
#     new_list_of_words = []
#     sentence = ""
#     for i in range(lenght):
#         word1 = random.choice(list_of_lines)
#         word1 = word1[0:-2].title()
#         new_list_of_words.append(word1)
#     for word in new_list_of_words:
#         sentence += word + " "
    
#     return sentence


# random_sentence1 = get_random_sentence(100)
# print(random_sentence1)


# # The words should be joined together into a string, which should be formatted in lower case (or title case) and returned.

# # Create a main function. It should:

# # Print a message explaining what the program does.

# # Ask the user how long the sentence should be. Acceptable values: an integer between 2 and 20.
# #  Validate your data, and test your validation!

# # If the user inputs incorrect data, print an error message and end the program.
# # If the user inputs correct data, user your functions to create a random sentence, 
# # and then display it proudly to the user.

# def mainFunction():
#     '''
#     Use this function to create a random sentence in within 2 and 20 characters. 
#     '''
#     valid_lenght = 0

#     while not 1 < valid_lenght < 21:
        
#         try :
#             valid_lenght = int(input("plese tell me how many words the sentence should have: "))    
#             if  not 1 < valid_lenght < 21:
#                 print("I told you to put a number between 2 and 20 @@@")
#             else:
#                 sentence_to = get_random_sentence(valid_lenght) 
#                 return sentence_to
#         except ValueError:
#             print("please enter a number")


# print(mainFunction())



















# Exercise 2: Working With JSON




sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

dict_sample = json.loads(sampleJson)


print(dict_sample["company"]["employee"]["payable"]["salary"])
dict_sample["company"]["employee"]["birth-date"] = "02-12-1988"


new_sample_jason = json.dumps(dict_sample)

with open("jsonFile1.txt", mode='w') as thefile:
    thefile.write(new_sample_jason)


# Access the nested key “salary” from the above JSON-string
# Add a key “birth_date” at the same level of the key “name”
# Save the dictionary as JSON to a file