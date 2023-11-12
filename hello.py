# first import the flask class
from flask import Flask

# creat an instance of this class
app = Flask(__name__)

# the use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"