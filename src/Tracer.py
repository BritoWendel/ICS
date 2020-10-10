VOWEL = "aeiou" 
VOWELACCENT = "áäàãéëèẽíïìĩóöòõúüùũ"
CONSONANTS = "bcdfghjklmnpqrstwxyz"
ALPHABET = VOWEL + VOWEL.upper() + VOWELACCENT + VOWELACCENT.upper() + CONSONANTS + CONSONANTS.upper()
NUMERIC = "1234567890"
ALPHANUMERIC = ALPHABET + NUMERIC
SYMBOLS = "!@#$%^&*()_-+=\\/?.,<>'\"[]{}"
SPACE = " "

class Tracer(object):
    def __init__(self, entry, rules):
        self.__rules = rules
        self.__entry = entry
        
        for i in range(2, len(self.__rules)):
            self.__rules[i][0] += i - 2
            self.__rules[1] += len(self.__rules[i][1])
    
    def __replace(self, value):
        self.__entry.delete(0, 'end')
        self.__entry.insert(0, value)

    def get(self):
        text = ""
        for char in self.__entry.get():
            if char in self.__rules[0]:
                text += char
        return text

    def set(self, value):
        len_value = len(value)
        for i in range(2, len(self.__rules)):
            rule = self.__rules[i]
            if len_value > rule[0]:
                value = value[:rule[0]] + rule[1] + value[rule[0]:]
                len_value += len(rule[1])
        self.__replace(value)

    def update(self, *args):
        text = self.__entry.get()
        len_text = len(text)

        if len_text == 0:
            return

        if text[-1] not in self.__rules[0] or len_text > self.__rules[1]:
            index = -2 if len_text > 1 and text[-2] == ')' else -1
            self.__replace(text[:index])
            return

        for rule in self.__rules[2:]:
            if len_text == (rule[0]+1):
                self.__replace(text[:-1] + rule[1] + text[-1])
                return

