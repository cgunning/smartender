import json
from classes import Pump

class Bartender:

    pumpConfig = json.load(open("config/pump_config.json"))
    drinkList = None
    drinkOptions = None
    loadedIngredients = None
    supportedDrinks = []
    pumps = {}

    def __init__(self, drinkList, drinkOptions):
        self.drinkList = drinkList
        self.drinkOptions = drinkOptions
        self.populateSupportedDrinks()
        self.setupPumps()
       

    def populateSupportedDrinks(self):
        self.supportedDrinks = []
        loadedIngredients = [self.pumpConfig[pump]["value"] for pump in self.pumpConfig.keys()]
        for drink in self.drinkList:
            supportedDrink = True
            for ingredient in drink["ingredients"].keys():
                if not ingredient in loadedIngredients:
                    supportedDrink = False
                    break
            if supportedDrink:
                self.supportedDrinks.append(drink)
        print(loadedIngredients)

    def getSupportedDrinks(self):
        return self.supportedDrinks

    def getPumps(self):
        return self.pumpConfig
    
    def setupPumps(self):
        for _, config in self.pumpConfig.items():
            self.pumps[config["value"]] = Pump.Pump(config["pin"], config["flow_rate"])
    
    def updatePumpDrink(self, pumpId, drink):
        self.pumpConfig[pumpId]["value"] = drink
        # TODO save to file
        self.populateSupportedDrinks()
        self.setupPumps()
    
    def getEstimatedPourTime(self, drinkKey):
        pourTime = 0
        for drink in self.supportedDrinks:
            if drink["key"] == drinkKey:
                for ingredient, amount in drink["ingredients"].items():
                    print(ingredient + ": " + str(self.pumps[ingredient].getEstimatedPourTime(amount)))
                    pourTime = max(pourTime, self.pumps[ingredient].getEstimatedPourTime(amount))
                break
        return pourTime
            

    def pour(self, drinkKey):
        drinkFound = False
        for drink in self.supportedDrinks:
            if drink["key"] == drinkKey:
                for ingredient, amount in drink["ingredients"].items():
                    print(ingredient + ":")
                    self.pumps[ingredient].pour(amount)
                drinkFound = True
                break
        return drinkFound