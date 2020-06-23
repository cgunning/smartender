import os
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

from classes import Bartender
from drinks import drinkList, drinkOptions
import json
import random
from classes import Pump


#if 'ENV' in os.environ.keys() and os.environ['ENV'] == "dev":


pumpConfig = json.load(open("config/pump_config.json"))
bartender = Bartender.Bartender(drinkList, drinkOptions)

drinklist = bartender.getSupportedDrinks()


def randomingredients():
    newdrinks = []
    newdrink = {}
    spirits = 0
    liquids = 0
    loadedIngredients = [pumpConfig[pump]["value"] for pump in pumpConfig.keys()]
    ingredients = random.sample(loadedIngredients, k=random.randint(2,6))
    for ingredient in ingredients:
        #print(ingredient)
        if ingredient in ("vodka", "gin", "rum"):
            amount = random.randint(1,100)
            if spirits + amount >= 100:
                amount = 100 - spirits
                spirits = 100
                newdrink[ingredient] = amount
            else:
                spirits += amount
                newdrink[ingredient] = amount
            newdrinks.append(newdrink)
            
        else:
            amount = random.randint(1,300)
            if liquids + amount >= 300:
                amount = 300 - liquids
                liquids = 300
                newdrink[ingredient] = amount
            else:
                liquids += amount
                newdrink[ingredient] = amount
            newdrinks.append(newdrink)
    
    threads = []
    self.led.setSpeed(200)        
    for thing in newdrink:
        print(ingredient + ":")
        threads.append(self.pumps[thing].pour(newdrink.get(thing)))
        drinkFound = True
        break
    for thread in threads:
        thread.join()
    self.led.setSpeed(0.8)
    
bartender.pour("randoming")