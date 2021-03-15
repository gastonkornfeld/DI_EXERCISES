from flask import Flask, render_template

# Using Flask, write a template for your CV.
# Your CV should contain:
# Your name
# A picture
# Your hobbies
# Your skills
# Your strengths
# Your weaknesses
# Bonus: Add some CSS
# Hint : To add some CSS look at the video Static Files in the Online Learning

app = Flask(__name__)

@app.route('/cv')
def print1_cv():
    return render_template("cv.html")

app.run(port=5001)



