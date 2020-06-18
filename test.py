import os
import sys
import fake_rpi

if 'ENV' in os.environ.keys() and os.environ['ENV'] == "dev":
    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

from classes import Bartender
from drinks import drinkList, drinkOptions
import json
import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
bartender = Bartender.Bartender(drinkList, drinkOptions)


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/drinks', methods=['GET'])
def getDrink():
    return render_template('drinks.html.j2', drinks=bartender.getSupportedDrinks())


@app.route('/pour', methods=['POST'])
def pourDrink():
    print(request.json["drink"])
    bartender.pour(request.json["drink"])
    return str(int(bartender.getEstimatedPourTime(request.json["drink"])))

@app.route('/pumps', methods=['GET'])
def getPumps():
    return render_template('pumps.html.j2', pumpConfig=bartender.getPumpConfig(), drinkOptions=bartender.getDrinkOptions())

@app.route('/pump', methods=['POST'])
def updatePump():
    bartender.updatePumpDrink(request.json["pump"], request.json["drink"])
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0")
