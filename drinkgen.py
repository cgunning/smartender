import json
import random
import codecs

def drinkGenerator(ingredients):
    result = []
    answer = ""
    with codecs.open('words.txt', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for word in data:
            oj = (data["oj"])
            gin = (data["gin"])
            vodka = (data["vodka"])
            rum = (data["rum"])
            coke = (data["coke"])
            tonic = (data["tonic"])
            alcohol = (data["alcohol"])
            drinks = (data["drinks"])
        running = True
        while running:        
            if "oj" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(oj))
            if "gin" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(gin))
            if "vodka" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(vodka))
            if "rum" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(rum))
            if "coke" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(coke))
            if "tonic" in ingredients:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(tonic))
            else:
                if random.randint(0,len(ingredients)) > len(ingredients) - 3:
                    result.append(random.choice(alcohol))
            if len(result) != 0:
                print("did i get here?")
                print(len(result))
                print(result)
                running = False
    if len(result) > 4:
        result = result[4:]
    for word in result:
        answer += word + " "
    return answer.encode('utf-8')

print(drinkGenerator(["vodka", "tonic", "coke","rum","gin","oj"]))
