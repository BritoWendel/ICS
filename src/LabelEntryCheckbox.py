from tkinter import *
from LabelEntry import *
from Checkbox import *
from ColumnSplitter import *

class LabelEntryCheckbox(Frame):
    def __init__(self, container, textLabel, textCheckbox):
        super().__init__(container)
        self.__cs0 = ColumnSplitter(container=self)
        self.__labelEntry = self.__cs0.addWidget(widget=LabelEntry(container=self.__cs0, textLabel=textLabel))
        self.__checkbox = self.__cs0.addWidget(widget=Checkbox(container=self.__cs0, textCheckbox=textCheckbox), weight=0, uniform='group2')
        self.__cs0.pack(fill='x')

    def getLabelEntryValue(self):
        return self.__cs0.getWidget(self.__labelEntry).getValue()

    def getCheckboxValue(self):
        return self.__cs0.getWidget(self.__checkbox).getValue()

