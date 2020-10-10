from tkinter import *

VOWEL = "aeiou" 
VOWELACCENT = "áäàãéëèẽíïìĩóöòõúüùũ"
CONSONANTS = "bcdfghjklmnpqrstwxyz"
ALPHABET = VOWEL + VOWEL.upper() + VOWELACCENT + VOWELACCENT.upper() + CONSONANTS + CONSONANTS.upper()
NUMERIC = "1234567890"
ALPHANUMERIC = ALPHABET + NUMERIC
SYMBOLS = "!@#$%^&*()_-+=\\/?.,<>'\"[]{}"
ALPHANUMERICSYMBOLIC = ALPHANUMERIC + SYMBOLS
SPACE = " "

class EEntry(Entry):
    def __init__(self, master, mask, lenght):
        self.__var = StringVar()
        super().__init__(master, textvariable=self.__var)
        self.__mask = mask
        self.__lenght = lenght
        self.__var.trace("w", self.__update)
        self.__rule_list = []

    def rule_add(self, pos, symbol):
        self.__rule_list.append([pos+len(self.__rule_list), symbol])
        self.__lenght += len(symbol)

    def get_raw(self):
        text = self.get()
        len_text = len(text)
        tmp_rule_list = [e for e in self.__rule_list]
        while len(tmp_rule_list) != 0:
            tmp_pos = tmp_rule_list[0][0]
            if len_text > tmp_pos:
                text = text[:tmp_pos] + text[tmp_pos+1:]
                del tmp_rule_list[0]
                for i in range(0, len(tmp_rule_list)):
                    if tmp_rule_list[i][0] > tmp_pos:
                        tmp_rule_list[i][0] -= 1
            else:
                del tmp_rule_list[0]
        print(text)
        return text

    def set_raw(self, value):
        len_value = len(value)
        for i in self.__rule_list:
            if len_value > i[0]:
                value = value[:i[0]] + i[1] + value[i[0]:]
                len_value += 1 
        self.value_replace(value)

    def value_replace(self, value):
        self.delete(0, END)
        self.insert(0, value)

    def __update(self, *args):
        text = self.get()
        len_text = len(text)
        len_rule = len(self.__rule_list)

        if len_text > 0:
            if len_text < self.__lenght:
                if (len_rule > 0):
                    for rule in self.__rule_list:
                        if len_text == (rule[0]+1):
                            final_text = text[:-1] + rule[1] + text[-1]
                            self.value_replace(final_text)
                        elif text[-1] == rule[1] or not text[-1] in self.__mask:
                            self.value_replace(text[:-1])
                    if len_rule > 0:
                        if text[-1] == self.__rule_list[-1][1]:
                            self.value_replace(text[:-1])
                else:
                    if not text[-1] in self.__mask:
                        self.value_replace(text[:-1])
            else:
                self.value_replace(text[:self.__lenght])

