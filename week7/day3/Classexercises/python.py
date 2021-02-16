
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

# Given a list of numbers, write a function that return the sum of every number.
#  BUT you can have a malicious string inside the list.


def sum_of_numbers(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        try:
            total += number
        except:
            print(f"{number}, is not a number.")

    return f"the total is:{total}"

print(sum_of_numbers(my_list))
