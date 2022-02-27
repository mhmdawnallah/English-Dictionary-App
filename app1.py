import json
from difflib import get_close_matches

class Translate:
    def __init__(self):
        self.file = open("data.json")
        try:
            self.data = json.load(self.file)
        except:
            print("Error Loading File")
    def translate(self,w):
        not_found_msg = "The word doesn't exit. Please double check it"
        if w in self.data:
            return self.data[w]
        elif get_close_matches(w,self.data.keys(),n=1):
            similar_word = get_close_matches(w,self.data.keys(),n=1)[0]
            ans = input("Did you mean %s [Y/N]: " % similar_word).lower()
            return self.data[similar_word] if ans in ['y',"yes"] else not_found_msg
        else:
            return not_found_msg
    def __del__(self):
        self.file.close()

word = input("Enter word: ").lower()  
result = Translate().translate(word)
print(*result, sep='\n'if isinstance(result, list) else '') 