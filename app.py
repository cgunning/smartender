from flask import Flask
from classes import Led
app = Flask(__name__)

pump1 = Led.Led(10, 40)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/drink")
def drink():
    pump1.run(5)
    return "Started"

if __name__ == "__main__":
    app.run()

