from tkinter import *
from LabelEntry import *
from ColumnSplitter import *

class TwoLabelEntry(Frame):
    def __init__(self, master, text, text1):
        super().__init__(master)
        self.__cs = ColumnSplitter(master=self)
        self.__cs.add(widget=LabelEntry(self.__cs, text=text))
        self.__cs.add(widget=LabelEntry(self.__cs, text=text1))
        self.__cs.pack(fill='x')

    def get(self, index):
        return self.__cs.get(index).get()

