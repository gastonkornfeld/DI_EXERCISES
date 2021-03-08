from datetime import timedelta
import datetime
import faker
# Create a function that displays the current date.
# Hint : Use the datetime module

def todayDay():   
    today = datetime.datetime.now()
    return today


print(todayDay())


# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st January is in 10 days and 10:34:01hours)


def betweenDays(start_date, end_date): 
    starting_date = datetime.date(start_date[2], start_date[1], start_date[0])
    ending_date = datetime.date(end_date[2], end_date[1], end_date[0])
    difference = (ending_date - starting_date).days
    # print(difference, "days")
    return difference

print(betweenDays([1,1,2021], [1,1,2022]))

def howMuchTill_1_Jan():
    #in hours, minutes, seconds
    today = todayDay()
    date2 = datetime.datetime((int(today.year)) + 1 , 1, 1)
    diff = date2 - today
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"hours: {hours} , minutes: {minutes} ,seconds: {seconds}, to the next first of january :)"
    
    
    # in days
    
    print(today)
    year1 = int(today.year)
    month1 = int(today.month)
    day1 = int(today.day)
    diference = betweenDays([day1, month1, year1], [1 , 1, year1 +1])
    print(f"there is {diference} days of difference")
    future_date = today + timedelta(days = diference)
    return diference

print(howMuchTill_1_Jan())


# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# and then display to the user the number of minutes he lived in his life.    

def how_many_minutes_you_lived(birthday):
    """
    must be get us [yyyy,mm,dd]
    """
    today = todayDay()
    birthday_year = birthday[0]
    birthday_month = birthday[1]
    birthday_day = birthday[2]
    date_birth = datetime.datetime(birthday_year, birthday_month, birthday_day)
    difference_bet = today - date_birth
    days = difference_bet.days
    hours = days * 24
    minutes = hours * 60
    
    return f"You lived {minutes} minutes already, amazing."
    

print(how_many_minutes_you_lived([2021, 3, 7]))






# Write a function that display today’s date,
#  the amount of time left from now until the next holiday, 
# additionally print what holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours)
# Hint: Start with hardcoding the datetime and name of the holiday


next_holidays = [[2021, 3, 10], [2021, 6, 23], [2021, 7, 22]]
    

def tillNextHoliday(dict_of_holidays):
    today_date = todayDay()
    print(today_date)
    first_date = datetime.datetime(dict_of_holidays[0][0], dict_of_holidays[0][1], dict_of_holidays[0][2])
    first_or_shorter_difference = first_date - today_date
    for holiday in dict_of_holidays:
        holiday_date = datetime.datetime(holiday[0], holiday[1], holiday[2])
        difference_with_holiday = holiday_date - today_date
        if difference_with_holiday < first_or_shorter_difference:
            first_or_shorter_difference = difference_with_holiday
    days, seconds = first_or_shorter_difference.days, first_or_shorter_difference.seconds
    hours = days * 24 + seconds // 3600
    return f"We have {days} days and {hours} hours left till next holiday" 

print(tillNextHoliday(next_holidays))











# Exercise 5 : How Old Are You In Jupiter ?
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, 
# you should be able to say that they’re 31.69 Earth-years old.


def years_around_the_world(seconds):
    """
    receive an amount of seconds someone lived and return his age in the different planets
    """
    
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365.25
    mercury_years = years / 0.2408467
    venus_years = years / 0.61519726
    mars_years = years / 1.8808158
    jupiter_years = years / 11.862615
    saturn_years = years / 29.447498
    uranus_years = years / 84.016846
    neptune_years = years / 164.79132
    print(f"you have {years} years in Earth ")
    print(f"you have {mercury_years} years in Mercury ")
    print(f"you have {venus_years} years in Venus ")
    print(f"you have {mars_years} years in mars ")
    print(f"you have {jupiter_years} years in Jupiter")
    print(f"you have {saturn_years} years in  Saturn")
    print(f"you have {uranus_years} years in  uranus")
    print(f"you have {neptune_years} years in neptune ")



years_around_the_world(100000000000)







# Install the faker module, and read the documentation.
# Create an empty list called users. Tip: It’s a list of dictionaries
# Create a function that adds dictionaries to the users list. Each user has the properties: 
# name, adress, langage_code. Use faker to populate them with fake data.

users = []


def addDictionary(list_of_dict):
    for i in range(10):
            
        new_dict = faker.Faker('it_IT')
        print(new_dict.name(), new_dict.address(), new_dict.language_code())
        list_of_dict.append(new_dict)
    return list_of_dict
    


print(addDictionary(users))