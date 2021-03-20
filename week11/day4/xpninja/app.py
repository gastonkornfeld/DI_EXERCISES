

from flask import Flask, render_template
import datetime

# Exercise 1: Fibonacci
# Instructions :
# Write a view that accepts a number X in the URL, 
# and then displays X numbers of the fibonacci sequence. Try to style it.

# Exercise 2: Dark Mode
# Instructions :
# Try to add a “dark mode” style to one of your sites.
# Try to implement an automatic dark mode activation between 20:00 and 08:00.

today = datetime.datetime.now()
hour = today.hour

def get_fibonacci(numbers):
    fib_numbers = [0,1]
    for i in range(2, numbers):
        fib_number = fib_numbers[i-1] + fib_numbers[i-2]
        fib_numbers.append(fib_number)
    return fib_numbers


print(get_fibonacci(10))



app = Flask(__name__)

@app.route('/<number>')
def fibonacci(number):
    number = int(number)
    numbers = get_fibonacci(number)
    return render_template('fibo.html', numbers=numbers, number=number, hour=hour)



app.run(debug=True, port=5002)
    








