from flask import Flask
from classes import Led
import RPi.GPIO as GPIO
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
pump1 = Led.Led(17, 4)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/drink")
def drink():
    pump1.run(5)
    return "Started"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

