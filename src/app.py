# A simple flask application to print hello world

#  loads the Flask framework so that you can use it
#
from flask import Flask, render_template

# creates a Flask application to run your code
#
app = Flask(__name__)

# Set to True if troubleshooting
#
app.config["DEBUG"] = True

# This decorator specifies that the following function defines what happens when someone goes to the location "/" on your site
#
@app.route('/')


# This simple function just says that when someone goes to the location, they get back the (unformatted) text "Hello from Flask."
#
def index():
    return render_template("main_page.html")

