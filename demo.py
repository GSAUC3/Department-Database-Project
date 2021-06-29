import json

data = json.load(open('jsons/btech.json'))
i='B8'
for j in data[i]:
    print(type(j),j )