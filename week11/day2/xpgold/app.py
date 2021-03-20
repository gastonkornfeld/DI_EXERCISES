


from flask import Flask, render_template
import datetime
from random import randint

today = datetime.datetime.now()
junfirst = datetime.datetime(today.year+1, 1, 1)
dif = junfirst - today

app = Flask(__name__)


@app.route('/date')
def date():
    return render_template('date.html', today = today)


@app.route('/random/<number>')
def random(number):
    cpu_number = randint(1,100)

    return render_template('random.html', number = int(number), cpu_number = cpu_number)


@app.route('/to1jan')
def dif():
    today = datetime.datetime.now()
    junfirst = datetime.datetime(today.year+1, 1, 1)
    dif = junfirst - today
    

    return render_template('tojanuary.html', dif = dif)


app.run(debug=True, port=5004)

