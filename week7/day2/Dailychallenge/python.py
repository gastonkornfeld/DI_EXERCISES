
import re

# Instructions
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column,
#  select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:
code_given = "7i3Tsih%xi #sM $a #t%^r!"
code_by_column=[]
for i in range (3):
    for index in range(len(code_given)):
        if index % 3 == i:
            code_by_column.append(code_given[index])

code_by_column = "".join(code_by_column)

result = re.sub(r"\W"," ", code_by_column)
result = re.sub(r"\d"," ", result)
# x = re.sub("'i(.+?)i'", " ",  code_by_column)
print(result)


