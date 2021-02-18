# import datetime


# # Exercise 7: When Will I Retire ?
# # The point of the exercise is to check is a person can retire depending on his age and his gender.
# # Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# # Create a function get_age(year, month, day)
# # Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# # After calculating the age of a person, the function should return it (the age is an integer).
# # Create a function can_retire(gender, date_of_birth).
# # It should call the get_age function (with what arguments?) in order to receive an age back.
# # Now it has all the information it needs in order to determine 
# # if the person with the given gender and date of birth is able to retire or not.
# # Calculate. You may need to do a little more hard-coding here.
# # Return True if the person can retire, and False if he/she can’t.
# # Some Hints

# # Ask for the user’s gender as “m” or “f”.
# # Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”.
# # Call can_retire to get a definite value for whether the person can or can’t retire.
# # Display a message to the user informing them whether they can retire or not.
# # As always, test your code to ensure it works


# year_of_birth = int(input("In wich year you born: "))
# month_of_birth = int(input("In wich month you born: "))
# day_of_birth = int(input("In wich day you born: "))
# gender = input("specefy your gender wit an f or m: ")
# mens_age_of_retirement = 67
# women_age_of_retirement = 62

# date_now = datetime.datetime.now()

# today_year = date_now.year
# today_month = date_now.month
# today_day = date_now.day
# user_age= 0
# def get_age(year, month, day):
#     user_age = today_year - year

#     if month > today_month:
#         user_age -= 1
#     elif month == today_month:
#         if day > today_day:
#             user_age -= 1
#         elif day == today_day:
#             print("Happy Birthday, your birthday is actually today")
            
#     return user_age



# print(get_age(year_of_birth, month_of_birth, day_of_birth))



# def can_retire(gender, year_of_birth, month_of_birth, day_of_birth):
#     actual_age = (get_age(year_of_birth, month_of_birth, day_of_birth))
    
#     if gender == "m":
#         if actual_age >= mens_age_of_retirement:
#             return True
#         else:
#             print(f"you need another {mens_age_of_retirement - actual_age} years to retire")
#             return False
#     elif gender == "f":
#         if actual_age >= mens_age_of_retirement:
#             return True
#         else:
#             print(f"you need another {women_age_of_retirement - actual_age} years to retire")
#             return False


# print(can_retire(gender, year_of_birth, month_of_birth, day_of_birth))










# Exercise 8:
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3 the output when calling our function should be 3702 (3 +33 +333 + 3333)
# Hint: treating our number as a int or a str at different points in our code may be helpful


number_to_play = input("wich with number you wanna play today: ")


def sum_of_concat(number):
    one = number
    two = str(number)*2
    three = str(number)*3
    four = str(number)*4
    total = int(one) + int(two) + int(three) + int(four)

    return f"{one} + {two} + {three} + {four} = {total}"



print(sum_of_concat(number_to_play))

