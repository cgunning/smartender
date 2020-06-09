from classes import Bartender
from drinks import drinkList, drinkOptions
import json
import random
from classes import Pump

pumpConfig = json.load(open("config/pump_config.json"))
bartender = Bartender.Bartender(drinkList, drinkOptions)

drinklist = bartender.getSupportedDrinks()

def randomdrink():
    return(random.choice(drinklist))
    
def randomingredients():
    newdrinks = []
    newdrink = {}
    spirits = 0
    liquids = 0
    loadedIngredients = [pumpConfig[pump]["value"] for pump in pumpConfig.keys()]
    ingredients = random.sample(loadedIngredients, k=random.randint(2,6))
    for ingredient in ingredients:
        print(ingredient)
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
            
    return(newdrink)
print(randomingredients())