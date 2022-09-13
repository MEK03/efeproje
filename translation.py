#TRANSLATION FROM TURKISH ALPHABET TO ENGLISH ALPHABET

def translate (phrase):
    tranlsation = ""
    for letter in phrase:
        if letter == "İ":
          tranlsation = tranlsation + "I"
        elif letter == "ö":
            tranlsation = tranlsation + "o"
        elif letter == "Ö":
            tranlsation = tranlsation + "O"
        elif letter == "Ü":
            tranlsation = tranlsation + "U"
        elif letter == "ü":
            tranlsation = tranlsation + "u"
        elif letter == "ğ":
            tranlsation = tranlsation + "g"

        else:
            tranlsation = tranlsation + letter

    return tranlsation


ph = input("Enter a word with Turkish alphabet characters:")

eng_phrase = translate(ph)

print("English alphabet equal is "+ eng_phrase)


