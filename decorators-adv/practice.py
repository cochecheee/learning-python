"""
High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif

Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif

Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif
"""

import random as rd
from flask import Flask

# randomly generate correct number
target = rd.randint(1,10)
# print(guessing)

app = Flask(__name__)

# create route for each number
@app.route('/')
def home():
    htmmlElement = "<h1>Guessing a number from 1 to 9 and add it to the end of home path</h1>" \
    "<p style='font-size: 1.2rem;'>Example: <b>htttps://fv.com/1 </b></p>"
    return htmmlElement

@app.route('/1')
def guessing_1():
    
    if target == 1:
        htmmlElement = "<h1>Correct answer!</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif target > 1: 
        htmmlElement = "<h1>You are too high!</h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        htmmlElement = "<h1>You are too low!</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    return htmmlElement

# same for 2 - 9
if __name__ == "__main__": 
    app.run(debug=True)
