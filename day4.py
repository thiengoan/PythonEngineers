from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/path")
def path():
    return "Hi Path"

if __name__ == "__main__":
    app.run()

