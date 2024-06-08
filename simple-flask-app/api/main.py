from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DesignX Developers😎"

@app.route("/about")
def about():
    return "Learn More About Me"