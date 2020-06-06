
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
    return render_template('drinks.html.j2', drinks=bartender.getSupportedDrinks())


@app.route('/pour', methods=['POST'])
def pourDrink():
    print(request.json["drink"])
    # bartender.pour
    return str(int(bartender.getEstimatedPourTime(request.json["drink"])))

@app.route('/pumps', methods=['GET'])
def getPumps():
    return json.dumps(bartender.getSupportedDrinks(), indent=2)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
