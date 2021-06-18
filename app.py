import json
from difflib import get_close_matches

data = json.load(open("C:/Users/David R. Abernathy/Desktop/python_projects/interactive_english_dictionary/data.json"))

def translate(w):
    w = w.lower() #accounts for user input that might not be all lowercase--converts user input to lowercase so the defintion is still returned
    if w in data:
        return data[w]
    elif w.title() in data: #checks for capitalized input as well
        return data[w.title()]
    elif w.upper() in data: #in case acronyms are entered
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yesno = input("Did you mean %s instead? Enter Y if yes, or N if no:  " % get_close_matches(w, data.keys())[0])
        if yesno == "Y":
            return data [get_close_matches(w, data.keys())[0]]
        if yesno == "N":
            return "This word doesnt exist.  Please try again!"
        elif yesno == "y":
            return data [get_close_matches(w, data.keys())[0]]
        elif yesno == "n":
            return "This word doesn't exist.  Please try again!"
        else:
            return "Sorry, but we didn't understand your entry!"
    else:
        return "Hm.  This doesn't seem to exist.  Please double check!"

word = input("Enter word:  ") #word is a global variable
output = (translate(word)) #global varial gets passed

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
