import re
import csv
import itertools


w = open('ip-ranges.json',mode='r')
region = set()
prefixHold = str()
newDict = {}

for i in w.readlines():
    if "prefix" in i:
        prefixHold = re.findall(r':\s"(.*)"', i)
    if "region" in i:
        regionHold = re.findall(r':\s"(.*)"', i)
        if regionHold[0] not in newDict:
            newDict[regionHold[0]] = [prefixHold[0]]
        else:
            newDict[regionHold[0]].append(prefixHold[0])


keys = sorted(newDict.keys())

with open('newFile.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(keys)
    writer.writerows(itertools.zip_longest(*[newDict[key] for key in keys]))

print(newDict)