from tkinter import *

class Checkbox(Frame):
    def __init__(self, master, text):
        super().__init__(master)
        self.__check_state = IntVar()
        self.__checkbox = Checkbutton(
                master=self, text=text, variable=self.__check_state, width=9)
        self.__checkbox.grid(row=1, column=0)
        self.rowconfigure(index=0, weight=1)

    def get(self):
        return bool(self.__check_state)

    def set(self, value):
        self.__check_state = IntVar(value)

