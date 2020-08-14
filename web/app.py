# A simple flask application to print hello world
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

# This simple function just says that when someone goes to the location, they get back the (unformatted) text "Hello from Flask."
#
def index():
    return render_template("main_page.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
