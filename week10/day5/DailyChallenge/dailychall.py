

import requests as req
import time

# Using the modules requests and time, create a function that returns 
# how long a webpage takes to load (how long it takes for a complete response to a request)
# Test your code with multiple sites such as google, ynet, imdb, etc.


def get_time_to_load(url):
    start = time.time()
    url1 = req.get(url)
    page = url1.text
    # print(page)
    end = time.time()

    time1 = end - start
    time1 = round(time1, 5)
    return f"The time to {url} to charge was: {time1} "



print(get_time_to_load("https://zetcode.com/python/requests/"))
print(get_time_to_load("https://www.webdesignerdepot.com/2013/04/20-wonderful-design-heavy-websites/"))
print(get_time_to_load("https://www.python.org/downloads/"))
print(get_time_to_load("https://www.youtube.com/"))
print(get_time_to_load("https://www.lavoz.com.ar/"))
print(get_time_to_load("https://www.ynet.co.il/home/0,7340,L-8,00.html"))
print(get_time_to_load("https://www.imdb.com/"))
print(get_time_to_load("https://dynomapper.com/blog/410-top-25-websites-to-learn-to-code"))
