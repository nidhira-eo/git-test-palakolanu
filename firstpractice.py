# app.py
from flask import Flask, render_template
from markupsafe import escape

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

@app.route("/hello/<name>")
def hello(name):
    return '<p>Hello, {}!</p>'.format(escape(name))

for rule in app.url_map.iter_rules():
    print(rule)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
