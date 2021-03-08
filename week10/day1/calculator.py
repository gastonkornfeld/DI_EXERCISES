

# from operators import addOperator as add
import operators

import request

token = "1665405087:AAHZBLPzpM79K7xDf9zeuXjlRrXwOxrBQyk"

get_me = f"https://api.telegram.org/bot{token}/getMe"

r = request.get(get_me)
print(r.text)
# print(add(2,3))

# print(operators.addOperator(3, 5))
# print(operators.divideOperator(24, 6))
# print(operators.print_hello())
# print(operators.bye())
# print(operators.substractOperator(99, 100))
# print(operators.multiplyOperator(2, 77))

# choose = ""
# while choose != "finish":
    
#     print("welcome to the calculator no negative result allowed")
#     print("a) ADD \nb) substract \nc) multiply \nd) divide, \n(finish) to end")
#     choose = input("choose an option: \n")
#     if choose == "a":
#         number1 = int(input("first number: "))
#         number2 = int(input("second number: "))
#         print(f"result = {operators.addOperator(number1, number2)}") 
#     elif choose == "b":
#         number1 = int(input("first number: "))
#         number2 = int(input("second number: "))
#         print(f"result = {operators.substractOperator(number1, number2)}")
#     elif choose == "c":
#         number1 = int(input("first number: "))
#         number2 = int(input("second number: "))
#         print(f"result = {operators.multiplyOperator(number1, number2)}")
#     elif choose == "d":
#         number1 = int(input("first number: "))
#         number2 = int(input("second number: "))
#         print(f"result = {operators.divideOperator(number1, number2)}")
#     elif choose == "finish":
#         print("bye")
#     else:
#         print("choose a valide option")