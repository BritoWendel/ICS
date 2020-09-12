from tkinter import *
from LabelEntry import *
from ColumnSplitter import *

class TwoLabelEntry(Frame):
    def __init__(self, container, textLabel0, textLabel1):
        super().__init__(container)
        self.__cs0 = ColumnSplitter(container=self)
        self.__widget0 = self.__cs0.addWidget(widget=LabelEntry(self.__cs0, textLabel=textLabel0))
        self.__widget1 = self.__cs0.addWidget(widget=LabelEntry(self.__cs0, textLabel=textLabel1))
        self.__cs0.pack(fill='x')

    def getLabelEntry0Value(self):
        return self.__cs0.getWidget(self.__widget0).getValue()

    def getLabelEntry1Value(self):
        return self.__cs0.getWidget(self.__widget1).getValue()

