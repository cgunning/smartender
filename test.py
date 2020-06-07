
from classes import Bartender
from drinks import drinkList, drinkOptions
import json
from flask import Flask, render_template, request
app = Flask(__name__)

bartender = Bartender.Bartender(drinkList, drinkOptions)


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/drinks', methods=['GET'])
def getDrink():
    return render_template('drinks2.html.j2', drinks=bartender.getSupportedDrinks())


@app.route('/pour', methods=['POST'])
def pourDrink():
    print(request.json["drink"])
    # bartender.pour
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
