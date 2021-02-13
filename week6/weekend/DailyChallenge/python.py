

# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
#  It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter 
# some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher,
#  the user entries the program, and then the program asks him if he wants to encrypt or decrypt,
#  and then execute encryption/decryption on a given message and a given shift.

# More information on caesar cipher is available on internet.

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)


print(ord(" "))
encriptyon_menu = ""
user_word = ""
final_word = ""
hoy_many = ""
all_results = []
while encriptyon_menu != "exit":
    encriptyon_menu =  input("Menu, wirte: \n exit: to exit \n  code: to code a frase \n  uncode: to uncode a frase\n What do you choose: ")
    if encriptyon_menu == "exit":
        print(all_results)
        break
    elif encriptyon_menu == "code":
        user_word = input('enter The frase to code:\n')
        hoy_many = int(input("how many characters you want to encrypt: "))
        for letter in user_word:
            ASCII_CODE = ord(letter)
            if ASCII_CODE == 32:
                final_letter = chr(ASCII_CODE)
                final_word += final_letter
            elif 96 < (ASCII_CODE + hoy_many) < 123:
                final_letter = chr(ASCII_CODE + hoy_many)
                final_word += final_letter
            else:
                final_letter = chr(ASCII_CODE + hoy_many - 26)
                final_word += final_letter
        print(final_word)
        all_results.append(final_word)
        final_word = ""
    elif encriptyon_menu == "uncode":
        user_word = input('enter The frase to uncode:\n')
        hoy_many = int(input("how many characters you want to uncrypt: "))
        for letter in user_word:
            ASCII_CODE = ord(letter)
            if ASCII_CODE == 32:
                final_letter = chr(ASCII_CODE)
                final_word += final_letter
            elif 96 < (ASCII_CODE - hoy_many) < 123:
                final_letter = chr(ASCII_CODE - hoy_many)
                final_word += final_letter
            else:
                final_letter = chr(ASCII_CODE - hoy_many + 26)
                final_word += final_letter
        print(final_word)
        all_results.append(final_word)
        final_word = ""

#  between 97 and 122
# 25 characters



   
