from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_template():
    year = datetime.now().year
    return render_template('index.html',year=year)

@app.route('/about')
def about():
    year = datetime.now().year
    return render_template('about.html',year=year)

@app.route('/contact')
def contact():
    year = datetime.now().year
    return render_template('contact.html',year=year)


if __name__ == '__main__':
    app.run(debug=True)