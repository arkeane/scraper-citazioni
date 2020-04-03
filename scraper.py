from bs4 import BeautifulSoup
import requests
import json
import sys

name=str(sys.argv[1])

url = 'https://it.wikipedia.org/wiki/{}'.format(name)
print (url)
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

author = content.find('h1', attrs={"class": "firstHeading"}).text

citArr = []

for cit in content.findAll('table', attrs={"class": "citazione-table"}):
	citObject = {
		"Author" : author,
		"text" : cit.find('p').text
	}
	citArr.append(citObject)

with open('citData.json','w', encoding='utf-8') as outfile:
	json.dump(citArr, outfile, ensure_ascii=False, indent=2)