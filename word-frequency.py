### Word-Frequency ###

with open("sample.txt") as infile:
    text_document = infile.read()

my_list = text_document.split()
print(my_list)

my_dict = {}

for word in my_list:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1
