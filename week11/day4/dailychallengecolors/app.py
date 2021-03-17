


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/red')
def red():
    return render_template('colorred.html')

@app.route('/blue')
def blue():
    return render_template('colorblue.html')

@app.route('/green')
def green():
    return render_template('colorgreen.html')

@app.route('/yellow')
def yellow():
    return render_template('coloryellow.html')






app.run(debug=True, port=5002)