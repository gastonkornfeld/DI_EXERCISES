
# filename = "names.txt"
# hola = open(filename, "w") #primero lo abro con r read como parametro
# hola.write("hello hello")
# hola.close()
# content2 = open(filename, "r")
# print(content2.read())
# content = hola.read() #luego lo leo y lo pongo en una variable

# print(content2)

# hola.close()












filename = "names.txt"

with open(filename, "r") as file_names:
    
    text = file_names.readlines()
    print(text[1])
    
    




# Modes:
# r - read (You cannot write in the file and the file has to exist)
# a - append (You can write in a file, everything you write will be added to
#               the end of the file)
# w - write (You can write in this file, but if you write something, you will erase all the current
#               content of the file)
# a and w modes create the file if it doesn't exist

# f = open(filename, "r")  # f is a FileObject (its an object representing the file)

# 2 ways to read a file:
# 1) Read the whole content of the file in one huge string (that contain the \n characters)
#content = f.read()
# You can read a file only once (read function empties the file buffer)

# 2) Read the lines of the file in a list
# lines = f.readlines()
# for line in lines:
#     print(line.strip()) # str.strip() removes all the trailing whitespaces/new line characters/tabs

# f.close()

# f = open(filename, "w")

# 2 Ways to write in a file (newlines are not automatically added)
# f.write("Hello World !\n")
#
# f.writelines(["Rick\n", "Summer\n", "Morty\n", "Beth\n"])
#
# f.close()

# The with keyword - temporary variable

# with open(filename, "r") as f:
#     print(f.readlines())

# Json and files:
import json

# json.dump({"name": "Eyal"}, open(filename, "w"))
# d = json.load(open(filename, "r"))
# print(d)