


import datetime

# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then:
# 2 Display him a little cake, like this:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles should be the last cypher of his age, if he is 53, then add 3 candles.

# Bonus : If he was born on a leap year, display two cakes !


user_birthday = ""

while user_birthday == "" or "/" not in user_birthday:
    user_birthday = input("Pelease Tell me your birthday in this format DD/MM/YYYY: \n")

 

user_birthday_day = int(user_birthday[0] + user_birthday[1])
user_birthday_month = int(user_birthday[3] + user_birthday[4])
user_birthday_year = int(user_birthday[6] + user_birthday[7] + user_birthday[8] + user_birthday[9])


print(user_birthday_day)
print(user_birthday_month)
print(user_birthday_year)



date_now = datetime.datetime.now()

today_year = date_now.year
today_month =date_now.month
today_day = date_now.day


user_age = today_year - user_birthday_year

if user_birthday_month > today_month:
    user_age -= 1
elif user_birthday_month == today_month:
    if user_birthday_day > today_day:
        user_age -= 1
    elif user_birthday_day == today_day:
        print("Happy Birthday, your birthday is actually today")

print(f"You have {user_age} years old")


amount_of_candles = int(str(user_age)[1])
amount_of__ = (int(5 - (amount_of_candles/2)) + 1) * "_"
amount_of_candles = "i" * amount_of_candles




print(f"        {amount_of__}{amount_of_candles}{amount_of__}\n       |:H:a:p:p:y:|\n     __|___________|__\n    |^^^^^^^^^^^^^^^^^|\n    |:B:i:r:t:h:d:a:y:|\n    |                 |\n    ~~~~~~~~~~~~~~~~~~~")




# Bonus
if user_birthday_year % 4 == 0:
    print(f"        {amount_of__}{amount_of_candles}{amount_of__}\n       |:H:a:p:p:y:|\n     __|___________|__\n    |^^^^^^^^^^^^^^^^^|\n    |:B:i:r:t:h:d:a:y:|\n    |                 |\n    ~~~~~~~~~~~~~~~~~~~")

