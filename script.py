# coding: utf-8

import xml.etree.ElementTree as ET

tree = ET.parse('Library.xml')
dicts = tree.findall("dict/dict/dict")

dictionaries = []
trackDictionary = {}
keys = []
values = []

for dict in dicts:
    for elem in dict:
        if elem.tag == 'key':
            keys.append(elem.text)
        else:
            values.append(elem.text)
    for i in range(0, len(keys)):
        trackDictionary[keys[i]] = values[i]
    dictionaries.append(trackDictionary)
    keys = []
    values = []
    trackDictionary = {}
    
artistNameList = []
i = 0
for dictionary in dictionaries:
    i += 1
    try:
        artistNameList.append(dictionary['Artist']+' - '+dictionary['Name'])
    except:
        artistNameList.append(dictionary['Name'])

artistNameList.sort()
for artistName in artistNameList:
    print(artistName)

f = open('Library.txt', 'w', encoding="utf-8")
for artistName in artistNameList:
    f.write(artistName + '\n')