



# Write a function named box_printer that takes any amount of strings 
# (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************

def box_printer(*args):
    variables = locals()
    list_of_variables = list(variables['args'])
    longest_string = max(list_of_variables, key=len)
    len_longest = len(longest_string)
    string_1_and_last = '*' * (len_longest + 7)
    print(string_1_and_last)
    for item in variables['args']:
        side_string = " " * (len_longest - len(item))
        print(f"*  {item} {side_string}  *")
    print(string_1_and_last)

    

box_printer("hola", "como", "estas",'me', 'gustaria', 'darte', 'un', 'lindo', 'mensaje')




def insertion_sort(alist):
   for index in range(1,len(alist)):

    currentvalue = alist[index]
    position = index

    while position>0 and alist[position-1]>currentvalue:
        alist[position]=alist[position-1]
        position = position-1

    alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)

