from tkinter import *

class LabelEntry(Frame):
    def __init__(self, container, textLabel):
        super().__init__(container)
        self.__label = Label(self, text=textLabel, anchor='w')
        self.__label.grid(row=0, column=0, stick='w')
        self.__entry = Entry(self)
        self.__entry.grid(row=1, column=0, stick='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def getValue(self):
        return self.__entry.get()

