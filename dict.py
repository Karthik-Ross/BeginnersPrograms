import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def transate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("Did you mean %s instead " %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no : ")
        if decide == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == 'n' :
            return("Sorry the word you entered is not available")
        else:
            return("You have entered an incorrect option")

    else:
        return("The word you want is not present here")

word = input("Enter the word to get its meaning : ")
output = transate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
