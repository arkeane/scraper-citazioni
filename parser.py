import json
import random

with open('citData.json') as json_data:
	jsonData = json.load(json_data)

print (random.choice(jsonData))

#for i in jsonData:
#	print (i['Author'])
#	print (i['text'])