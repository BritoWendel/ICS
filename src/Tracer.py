VOWEL_LOWER = "aeiou"
VOWEL_UPPER = VOWEL_LOWER.upper()
VOWEL = VOWEL_LOWER + VOWEL_UPPER
VOWEL_ACCENT_LOWER = "áäàãéëèẽíïìĩóöòõúüùũ"
VOWEL_ACCENT_UPPER = VOWEL_ACCENT_LOWER.upper()
VOWEL_ACCENT = VOWEL_ACCENT_LOWER + VOWEL_ACCENT_UPPER
VOWEL_FULL = VOWEL + VOWEL_ACCENT
CONSONANTS_LOWER = "bcçdfghjklmnpqrstvwxyz"
CONSONANTS_UPPER = CONSONANTS_LOWER.upper()
CONSONANTS = CONSONANTS_LOWER + CONSONANTS_UPPER
ALPHABET = VOWEL_FULL + CONSONANTS 
NUMERIC = "1234567890"
ALPHANUMERIC = ALPHABET + NUMERIC
SYMBOLS = "!@#$%^&*()_-+=\\/?.,<>'\"[]{}"
SPACE = " "

class Tracer(object):
    def __init__(self, entry, rules, zeroes=None):
        self.__rules = rules
        self.__entry = entry
        self.__zeroes = zeroes
        
        for i in range(2, len(self.__rules)):
            self.__rules[i][0] += i - 2
            self.__rules[1] += len(self.__rules[i][1])
    
    def __replace(self, value):
        self.__entry.delete(0, 'end')
        self.__entry.insert(0, value)

    def get(self, entry_value=None):
        text = ""
        if entry_value == None:
            entry_value = self.__entry.get()

        if entry_value == "":
            return entry_value

        for char in entry_value:
            if char in self.__rules[0]:
                text += char
        return text

    def set(self, value):
        len_value = len(value)
        real_size = self.__rules[1] - len(self.__rules[2:])
        zero_increment = ""
        if (len_value < real_size and
            self.__rules[0] == NUMERIC and
            self.__zeroes != None):
            for i in range(real_size-len_value):
                zero_increment += "0"
            value = zero_increment + value
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
            if len_text > 1 and (text[-2] == ')' or text[-2] == ' '):
                if text[-3] == ';':
                    index = -3
                else:
                    index = -2
            else:
                index = -1
            self.__replace(text[:index])
            return

        for rule in self.__rules[2:]:
            if len_text == (rule[0]+1):
                self.__replace(text[:-1] + rule[1] + text[-1])
                return

