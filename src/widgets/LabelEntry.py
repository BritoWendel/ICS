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

class LabelEntry(Frame):
    def __init__(self, master, text, mask, lenght):
        super().__init__(master)
        self.__label = Label(master=self, text=text, anchor='w')
        self.__label.grid(row=0, column=0, stick='w')
        self.__var = StringVar()
        self.__mask = mask
        self.__lenght = lenght
        self.__entry = Entry(self, textvariable=self.__var)
        self.__var.trace("w", lambda name, index, mode, var=self.__var:self.__update())
        self.__entry.grid(row=1, column=0, stick='nsew')
        self.__rule_list = []
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

    def rule_add(self, pos, symbol):
        self.__rule_list.append([pos+len(self.__rule_list), symbol])
        self.__lenght += len(symbol)
        return self

    def multiple_rule_add(self, rules):
        for rule in rules:
            self.rule_add(rule[0], rule[1])

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
        return text

    def set_raw(self, value):
        len_value = len(value)
        for i in self.__rule_list:
            if len_value > i[0]:
                value = value[:i[0]] + i[1] + value[i[0]:]
                len_value += 1 
        self.set(value)
                
    def get(self):
        return self.__entry.get()

    def set(self, value):
        self.__entry.delete(0, END)
        self.__entry.insert(0, value)

    def insert(self, value):
        text = self.get()
        self.__entry.insert(END, value)
        self.__entry.icursor(len(text)+1)

    def focus(self):
        self.__entry.focus()

    def __update(self):
        text = self.get()
        len_text = len(text)
        len_rule = len(self.__rule_list)

        if len_text > 0:
            if len_text < self.__lenght:
                if (len_rule > 0):
                    for rule in self.__rule_list:
                        if len_text == (rule[0]+1):
                            final_text = text[:-1] + rule[1] + text[-1]
                            self.set(final_text)
                        elif text[-1] == rule[1] or not text[-1] in self.__mask:
                            self.set(text[:-1])
                else:
                    if not text[-1] in self.__mask:
                        self.set(text[:-1])
            else:
                self.set(text[:self.__lenght])

            if len_rule > 0:
                if text[-1] == self.__rule_list[-1][1]:
                    self.set(text[:-1])

