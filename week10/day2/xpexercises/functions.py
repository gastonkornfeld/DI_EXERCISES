

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





