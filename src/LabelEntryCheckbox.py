from tkinter import *
from LabelEntry import *
from Checkbox import *
from ColumnSplitter import *

class LabelEntryCheckbox(Frame):
    def __init__(self, master, text, text1):
        super().__init__(master)
        self.__cs = ColumnSplitter(master=self)
        self.__cs.add(widget=LabelEntry(master=self.__cs, text=text))
        self.__cs.add(widget=Checkbox(master=self.__cs, text=text1), weight=0, uniform='g2')
        self.__cs.pack(fill='x')

    def get(self, index):
        return self.__cs.get(index).get()

