
### Word-Frequency ###

import operator
mydict = {}

with open("sample.txt") as infile:
    document = infile.read().replace(".","").replace("?","").replace("!","").lower()
for word in document.split():
    if word not in mydict.keys():
        mydict[word] = 0
    mydict[word] += 1

sorted_dict = sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)

for index in range(20):
    print(sorted_dict[index])
