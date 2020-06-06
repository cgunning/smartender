from flask import Flask
#from classes import Led
import RPi.GPIO as GPIO
from classes/rgbled import rgbled
from random import randint
import time

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
led = rgbled(17,27,22)

@app.route("/")
def hello():
    led.off(0.8)
    led.cleanup()
    return "Hello World!"

@app.route("/drink")
def drink():
    while True:
        r = randint(0,100)
        g = randint(0,100)
        b = randint(0,100) 
        led.changeto(r,g,b,0.8)
        time.sleep(2)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

