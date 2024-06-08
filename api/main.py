from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DesignX Developers😎"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
