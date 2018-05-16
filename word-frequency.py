
### Word-Frequency ###

mydict = {}

with open("sample.txt") as infile:
    document = infile.read().replace(".","").replace("?","").replace("!","").lower()
for word in document.split():
    if word not in mydict.keys():
        mydict[word] = 0
    mydict[word] += 1
sorted_dict = sorted(mydict.items())
for word, count in mydict.items():
    print("{} {}".format(word, count))
