import json

f = open('words.json')
g = open('output.txt', 'a')
data = json.load(f)

size = int(input("Enter size of username required: "))
for i in range(0, len(data)):
    if len(data[i]) == size:
        g.write(data[i] + "\n")
        continue
    elif len(data[i]) > size:
        continue
    for j in range(i+1, len(data)):
        if len(data[j]) == size:
            g.write(data[j] + "\n")
            continue
        elif len(data[j]) > size:
            continue
        elif len(data[i] + data[j]) == size:
            g.write(data[i] + data[j] + "\n")
            g.write(data[j] + data[i] + "\n")

f.close()
g.close()
