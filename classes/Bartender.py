import json
import threading
import random
import codecs
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
    global drinkjson 

    def __init__(self, drinkList, drinkOptions):
        self.drinkList = drinkList
        self.drinkOptions = drinkOptions
        self.populateSupportedDrinks()
        self.setupPumps()
        self.led.run()
        self.stopAllPumps()

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

    def getEstimatedPourTime(self, drink):
        pourTime = 0
        for ingredient, amount in drink["ingredients"].items():
            #print(ingredient + ": " + str(self.pumps[ingredient].getEstimatedPourTime(amount[0])))
            pourTime = max(pourTime, self.pumps[ingredient].getEstimatedPourTime(amount[0]))
        return pourTime
        
    def drink2json(self, drink):
        #print(drink)
        res = json.dumps(drink, indent=4)
        global drinkjson 
        self.drinkjson = res
        
    def getDrinkJson(self):
        global drinkjson
        return str(self.drinkjson)

    def pour(self, drinkKey):
        t = threading.Thread(target=self.pourInternal, args=(drinkKey,))
        t.start()
        return t
    
    def startPump(self, pumpId):
        pumpPin = self.pumpConfig[pumpId]["pin"]
        for ingredient, pump in self.pumps.items():
            if pump.pin == pumpPin:
                pump.start()
                return
    
    def stopPump(self, pumpId):
        pumpPin = self.pumpConfig[pumpId]["pin"]
        for ingredient, pump in self.pumps.items():
            if pump.pin == pumpPin:
                pump.stop()
                return
    
    
    def startAllPumps(self):
        for ingredient, pump in self.pumps.items():
            pump.start()
    
    def stopAllPumps(self):
        for ingredient, pump in self.pumps.items():
            pump.stop()

    def pourInternal(self, drinkKey):
        drinkFound = False
        threads = []
        if drinkKey == "randoming":
            drink = self.randomIngredients()
            for ingredient, amount in drink["ingredients"].items():
                for name in self.drinkOptions:
                    if ingredient == name["value"]:
                        drink["ingredients"][ingredient] = [amount, name["name"]]
            drink["duration"] = self.getEstimatedPourTime(drink)
            self.drink2json(drink)
            self.led.setSpeed(200)
            for ingredient, amount in drink["ingredients"].items():
                print(ingredient + ":")
                threads.append(self.pumps[ingredient].pour(amount))
            drinkFound = True
        else:   
            for drink in self.supportedDrinks:
                if drink["key"] == drinkKey:
                    for ingredient, amount in drink["ingredients"].items():
                        for name in self.drinkOptions:
                            if ingredient == name["value"]:
                                drink["ingredients"][ingredient] = [amount, name["name"]]
                    drink["duration"] = self.getEstimatedPourTime(drink)
                    self.drink2json(drink)
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
    
    def drinkGenerator(self):
        result = []
        with codecs.open('words2.txt', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for word in data:
                det = (data["det"])
                adj = (data["adj"])
                noun = (data["noun"])
            
            deter = random.choice(det)
            adje = random.choice(adj)
            nou = random.choice(noun)        
            return (adje + " " + nou)
                
    
    def randomIngredients(self):
        newdrinks = []
        name = self.drinkGenerator()
        newdrink = {"name": "test", 
                            "ingredients": {}                             
                            }
        newdrink["name"] = name
        spirits = 0
        liquids = 0
        loadedIngredients = [self.pumpConfig[pump]["value"] for pump in self.pumpConfig.keys()]
        ingredients = random.sample(loadedIngredients, k=random.randint(2,6))
        for ingredient in ingredients:
            if ingredient in ("vodka", "gin", "rum", "requila", "trisec", "appschnaps", "peachschnaps"):
                amount = random.randint(1,100)
                if spirits + amount >= 100:
                    amount = 100 - spirits
                    spirits = 100
                else:
                    spirits += amount
            else:
                amount = random.randint(1,300)
                if liquids + amount >= 300:
                    amount = 300 - liquids
                    liquids = 300
                else:
                    liquids += amount
            if amount != 0:
                if amount < 10:
                    amount = 10
                newdrink["ingredients"][ingredient] = amount
        newdrinks.append(newdrink)
        return newdrink
        
    
