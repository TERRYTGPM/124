from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "hell-o"

def he():
    return 'eeeee'

if __name__ == "__main__":
    app.run()