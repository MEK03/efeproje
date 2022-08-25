dict = {}
str = input("Enter the word: ")
for i in str:
    words = dict.keys()
    if i in words:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

print(dict)
