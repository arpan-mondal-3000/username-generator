import json

f = open('words.json')
data = json.load(f)

for word in data:
    print(word)

f.close()
