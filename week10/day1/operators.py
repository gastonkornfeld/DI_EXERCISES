

# Create a file called operators.py

# Create 2 functions : addOperator() 
# that returns the addition of 2 numbers, and divideOperator() that returns the division of 2 numbers

# Create another file called calculator.py, 
# and import the operators module. Call the 2 functions and display the results

# Do this process 3 times : once by importing the whole module, 
# the second time by importing specific functions, the third time by using alias


def print_hello():
    return "hello we are learning modules with python"

def bye():
    return "bye bye"

def addOperator(number, second_number):
    if number + second_number > 0:
        return number + second_number
    else:
        return 0


def substractOperator(number, second_number):
    if number - second_number > 0:
        return number - second_number
    else:
        return 0

def multiplyOperator(number, second_number):
    if number * second_number > 0:
        return number * second_number
    else:
        return 0

def divideOperator(number, second_number):
    try:
        number / second_number
    except: 
        print("put two numbers or try not to divide by zero")
    else:
        if number / second_number > 0:
            return number / second_number
        else:
            return 0