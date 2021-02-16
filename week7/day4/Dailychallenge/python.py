



# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Buit-in exceptions of Python : Look here


def divide_by_zero(number):
    try:
        a = number/0
    except ZeroDivisionError:
        print("You cant divide by zero")
        a = 0
    return number

print(divide_by_zero(9))

