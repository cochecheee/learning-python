from flask import Flask, render_template
# Flask has a method called request (don't confuse this with the requests module)
from flask import request as req

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# CHALLENGE: See if you can use the documentation below to figure out how to make our HTML form submit a "POST" request to the path "/login".
@app.route('/login',methods=["POST"])
def login():
    if req.method == 'POST':
        username = req.form['name']
        password = req.form['password']
        print(username +  password)
        return f"💪 Success! Form submitted. Your username id {username} and password is {password}"
    else:
        return "<h1>Fail to make POST request to server</h1>"
if __name__ == '__main__':
    app.run(debug=True)