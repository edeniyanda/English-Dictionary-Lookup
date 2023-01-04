import json 
from difflib import get_close_matches


data = json.load(open("dictionary_compact.json"))

try_again = True

while True:
    word = input ("Enter a word:").lower()
    closematch = get_close_matches(word, data, n=4)


    def translate(x):
        global try_again
        
        if x in data:
            cap_x = x.upper()
            return f"According to Webster English Dictionary,\n{cap_x} means - {data[x]}"

        elif len(closematch) > 0:
            return f"'{x}' does not exixt\nDo you mean one of these {closematch}?"
        
        elif len(x) == 0 :
            try_again = False 
            return("Bye")
        
        else:
            return f"'{x}' does not exist"

    print(translate(word))
    
    if not try_again:
        break


    
    
