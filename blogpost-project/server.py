#link post: https://www.npoint.io/docs/c790b4d5cab58020d391

# solution: https://gist.github.com/TheMuellenator/7c6a08a3df3b94a28d1a867628481910
from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/post/<int:id_no>')
def blog_posts(id_no):
    pass


if __name__ == "__main__":
    app.run(debug=True) 