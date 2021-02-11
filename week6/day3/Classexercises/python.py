# # Given this list: list1 = [5, 10, 15, 20, 25, 50, 20], find value 20 in the list,
# #  and if it is present, replace it with 200. Only update the first occurrence of a value

# # Hint : Look at the index method


# list1 = [5, 10, 15, 20, 25, 50, 20]

# position_of_20 = list1.index(20)

# list1[position_of_20] = 200

# print (list1)

# print(sorted(list1, reverse=True))










# # Unpack the following tuple into 4 variables


# aTuple = (10, 20, 30, 40)

# a, b, c, d = aTuple

# print(a)
# print(b)
# print(c)
# print(d)












# Accept n number from user and print its multiplication table

# first solution
user_number = int(input('Tell me a number: \n'))
# result = 1
# for i in range(0, 21):
#     result = (user_number * i)
#     print(f"{user_number} x {i} = {result}")
# second solution to the same problem
# initial = 0
# while initial < user_number * 20: #first 20 multipliers
#     print(initial)
#     initial += user_number














# Print first 10 numbers using while loop


initial = 0
while initial < 11:
    print(initial)
    initial += 1






