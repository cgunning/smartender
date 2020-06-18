import json
import threading
from classes import Pump
from classes import rgbled

class Bartender:
    pumpConfigFile = "config/pump_config.json"
    led = rgbled.rgbled(17,27,22)
    pumpConfig = json.load(open(pumpConfigFile))
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
        self.led.run()

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

    def getPumpConfig(self):
        return self.pumpConfig

    def getDrinkOptions(self):
        return self.drinkOptions
    
    def setupPumps(self):
        for _, config in self.pumpConfig.items():
            self.pumps[config["value"]] = Pump.Pump(config["pin"], config["flow_rate"])
    
    def updatePumpDrink(self, pumpId, drink):
        self.pumpConfig[pumpId]["value"] = drink
        self.savePumpConfig()
        self.populateSupportedDrinks()
        self.setupPumps()
    
    def savePumpConfig(self):
        with open(self.pumpConfigFile, 'w') as outfile:
            json.dump(self.pumpConfig, outfile, indent=2)

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
        t = threading.Thread(target=self.pourInternal, args=(drinkKey,))
        t.start()
        return t

    def pourInternal(self, drinkKey):
        drinkFound = False
        threads = []
        for drink in self.supportedDrinks:
            if drink["key"] == drinkKey:
                self.led.setSpeed(200)
                for ingredient, amount in drink["ingredients"].items():
                    print(ingredient + ":")
                    threads.append(self.pumps[ingredient].pour(amount))
                drinkFound = True
                break
        for thread in threads:
            thread.join()
        self.led.setSpeed(0.8)

        return drinkFound