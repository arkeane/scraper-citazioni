import json

with open('citData.json') as json_data:
	jsonData = json.load(json_data)

for i in jsonData:
	print (i['Author'])
	print (i['text'])