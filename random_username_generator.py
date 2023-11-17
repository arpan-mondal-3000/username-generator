import random
import json

f = open('words.json')
data = json.load(f)
size = int(input("Enter number of usernames to be generated randomly: "))
for i in range(0, size):
    print(data[random.randint(0, len(data))] +
          data[random.randint(0, len(data))])

f.close()
