# Instruction: Information From The User
# Notice : solve this using a lambda function, even if you can think of another way
# Hint: Look at the lesson on Week4Day4

# Take the following inputs 5 times from the user:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple will contain a name, age and score
# Sort the list by the following priority Name > Age > Score
def swap_position(list1, pos1, pos2):

    first_elem = list1.pop(pos1)
    secon_elem = list1.pop(pos2-1)
    list1.insert(pos1, secon_elem)
    list1.insert(pos2, first_elem)
    return list1


def divide_data(item):
    '''
    used to divide the information in to 3 lists
    '''
    for i in range(len(item[0])):
        for j in range(len(item)):
            if i == 0:
                list_of_names.append(item[j][i])
            elif i == 1:
                list_of_ages.append(item[j][i])
            elif i == 2:
                list_of_score.append(item[j][i])



list_of_tuples= []    


for i in range(5):
    name = input("Name:")
    age = input("Age:")
    score = input("Score:")
    user_inf = (name, age, score)
    list_of_tuples.append(user_inf)

list_of_names = []
list_of_ages = []
list_of_score = []
    
divide_data(list_of_tuples)
    
sort_list = lambda list1: sorted(list1)
chek_if_repeat = lambda list1: not (len(list1) == len(list(set(list1))))

names_sorted = sort_list(list_of_names)
# print(names_sorted)
final_order = []


# # quiero agarrar el primer elemento del nombre, 
# # buscarlo en las tuplas, y luego agarrar esa tupla y ponerla en la posicion primera
if not chek_if_repeat(list_of_names):
    for i in range(len(names_sorted)):
        for j in range(len(list_of_tuples)):
            if names_sorted[i] == list_of_tuples[j][0]:
                final_order.append(list_of_tuples[j])
    print(final_order)    




if chek_if_repeat(list_of_names):
    for i in range(len(list_of_tuples)):

        for i in range(len(list_of_names)-1):
            if list_of_names[i] == list_of_names[i + 1]:
                if list_of_ages[i] < list_of_ages[i + 1]:
                    swap_position(list_of_ages, i, i+1)
                    swap_position(list_of_names, i, i+1)
                    swap_position(list_of_score, i, i+1)
                elif list_of_ages[i] == list_of_ages[i+1]:
                    if list_of_score[i] < list_of_score[i + 1]:
                        swap_position(list_of_ages, i, i+1)
                        swap_position(list_of_names, i, i+1)
                        swap_position(list_of_score, i, i+1)
                    
                    



final_order = (list_of_names, list_of_ages, list_of_score)
print(final_order)
for i in range(len(list_of_tuples)):
    print(f"number {i + 1}")
    print(list_of_names[i], list_of_ages[i], list_of_score[i])
    print("\n")











