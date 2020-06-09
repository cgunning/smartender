import json
import random
import codecs

def drinkGenerator(ingredients):
    result = ""
    with codecs.open('words.txt', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for word in data:
            oj = (data["oj"])
            gin = (data["gin"])
            vodka = (data["vodka"])
            rum = (data["rum"])
            coke = (data["coke"])
            tonic = (data["tonic"])
        running = True
        while running:        
            if "oj" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 2:
                    result += random.choice(oj) + " "
            if "gin" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 2:
                    result += random.choice(gin) + " "
            if "vodka" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 2:
                    result += random.choice(vodka) + " "
            if "rum" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 2:
                    result += random.choice(rum) + " "
            if "coke" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 2:
                    result += random.choice(coke) + " "
            if "tonic" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 2:
                    result += random.choice(tonic) + " "
            if result != "":
                running = False
    
    return result.encode('utf-8')

print(drinkGenerator(["vodka", "tonic", "coke","rum","gin","oj"]))
