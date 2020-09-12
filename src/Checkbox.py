from tkinter import *

class Checkbox(Frame):
    def __init__(self, container, textCheckbox):
        super().__init__(container)
        self.__isCheck = IntVar()
        self.__checkbox = Checkbutton(self, text=textCheckbox, variable=self.__isCheck, width=9)
        self.__checkbox.grid(row=1, column=0)
        self.rowconfigure(0, weight=1)

    def getValue(self):
        return bool(self.__isCheck)

