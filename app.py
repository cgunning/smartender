from flask import Flask
#from classes import Led
import RPi.GPIO as GPIO
from classes import rgbled
from random import randint
import time

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
pump1 = rgbled(17,27,22)

@app.route("/")
def hello():
    pump1.off(0.8)
    pump1.cleanup()
    return "Hello World!"

@app.route("/drink")
def drink():
    try:
    while True:
        r = randint(0,100)
        g = randint(0,100)
        b = randint(0,100)
        pump1.changeto(r,g,b,0.8)
        time.sleep(2)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

