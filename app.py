from flask import Flask
#from classes import Led
import RPi.GPIO as GPIO
from rgbled import rgbled
from random import randint
import time
import threading

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
led = rgbled(17,27,22)


@app.route("/")
def hello():
    return("Hello World!")

@app.route("/drink")
def drink():

    return("drink")

@app.route("/slow")
def slow():
    led.setSpeed(0.8)
    return("slow")

@app.route("/fast")
def fast():
    led.setSpeed(200)
    return("fast")

if __name__ == "__main__":
    led.run()
    app.run(host="0.0.0.0")
