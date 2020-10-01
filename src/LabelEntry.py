from tkinter import *

class LabelEntry(Frame):
    def __init__(self, master, text, mask, max_lenght):
        super().__init__(master)
        self.__label = Label(master=self, text=text, anchor='w')
        self.__label.grid(row=0, column=0, stick='w')
        self.__var = StringVar()
        self.__mask = mask
        self.__max_lenght = max_lenght
        self.__entry = Entry(self, textvariable=self.__var)
        self.__var.trace("w", lambda name, index, mode, var=self.__var:self.__update())
        self.__entry.grid(row=1, column=0, stick='nsew')
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

    def get(self):
        return self.__entry.get()

    def set(self, value):
        self.__entry.delete(0, END)
        self.__entry.insert(0, value)

    def insert(self, value):
        text = self.get()
        self.__entry.insert(END, value)
        self.__entry.icursor(len(text)+1)

    def __update(self):
        text = self.get()
        len_text = len(text)

        if len_text > 0:
            if len_text < self.__max_lenght:
                for rule in format_rules:
                    if len_text == 2:#rule.position
                        self.insert(':')#rule.symbol
                    elif text[-1] == ':' or not text[-1] in self.__mask:
                        self.set(text[:-1])
            else:
                self.set(text[:self.__max_lenght])

