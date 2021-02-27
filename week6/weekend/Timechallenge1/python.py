




# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.
# Take a number as input from user and print whether it is a perfect number or not. 
# If yes then print True else False.

# Hint: Google perfect numbers

def perfectNumber (number):
    sum_divisors = 0
    divisors_of_number = []
    for i in range (1, int(number/2) + 1):
        if number % i == 0:
            sum_divisors += i
            divisors_of_number.append(i)
    if sum_divisors == number:
        return True, f"for the number {number}"
    else:
        return f"for the number {number} the sum of the divisors is {sum_divisors} \n list of divisors: {divisors_of_number}"



print(perfectNumber(100))
print(perfectNumber(88))
print(perfectNumber(6))
print(perfectNumber(123))
print(perfectNumber(8128))
print(perfectNumber(44))
print(perfectNumber(33))
print(perfectNumber(20))
print(perfectNumber(496))
print(perfectNumber(1000))
print(perfectNumber(10000))
print(perfectNumber(100000))
