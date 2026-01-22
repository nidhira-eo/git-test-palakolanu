# app.py
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define a route and a function 
# to handle it
@app.route('/')
def hello_world():
    return '<h1>Hello!</h1>'

@app.route("/about")
def about():
    return '<h1>We are united!</h1>'

@app.route("/greet/<username>")
def greet(username):
    return render_template("greet.html", name=username)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
