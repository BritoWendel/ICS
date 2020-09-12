from tkinter import *

class ColumnSplitter(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__widgets = []
        self.grid_rowconfigure(0, weight=1)

    def addWidget(self, widget, weight=1, uniform='group1'):
        self.__widgets.append(widget)
        list_size = len(self.__widgets) - 1
        self.grid_columnconfigure(list_size, weight=weight, uniform=uniform)
        self.__widgets[list_size].grid(row=0, column=list_size, stick='nsew')

    def getWidget(self, index):
        return self.__widgets[index]

