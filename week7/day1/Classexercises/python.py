# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call





def calculation(num1, num2):
    sum2 = num1 + num2
    subst = num1 - num2
    print(f"{num1} + {num2} = {sum2}")
    print(f"{num1} - {num2} = {subst}")
    return "Done"

print(calculation(799, 4553468))
