from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():

    return "Hello, this is a sample Web App devloped in Pyhton and Flask to showcase CI CD workflow"


