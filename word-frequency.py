### Word-Frequency ###


with open("sample.txt") as infile:
    wordcounter = {}
    for word in infile.read().split():
        if word not in wordcounter:
            wordcounter[word] = 0
        wordcounter[word] += 1
    print(wordcounter)
