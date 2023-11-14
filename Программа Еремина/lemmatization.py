import json
from pymystem3 import Mystem
import words


myst = Mystem()

def diction_form(text): #лемматизация
    text = ''.join(myst.lemmatize(text)).rstrip('\n')
    return text

x = []
y = []
for intent in words.INTENTS: #заполняем листы примерами входных текстов и соответствующими намерениями
    print("Гружусь...")
    examples = words.INTENTS[intent]["examples"]
    for example in examples:
        word= diction_form(example)
        x.append(word)
        y.append(intent)

with open('json/x.json', 'w') as filehandle:
    json.dump(x, filehandle)

with open('json/y.json', 'w') as filehandle:
    json.dump(y, filehandle) 