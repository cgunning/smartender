import json
import random
import codecs

def drinkGenerator():
    result = []
    answer = ""
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
for i in range(0,10):
    print(drinkGenerator())