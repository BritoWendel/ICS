from tkinter import *

class ColumnSplitter(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__widgets = []
        self.grid_rowconfigure(index=0, weight=1)

    def add(self, widget, weight=1, uniform='g1'):
        self.__widgets.append(widget)
        list_size = len(self.__widgets) - 1
        self.grid_columnconfigure(index=list_size, weight=weight, uniform=uniform)
        self.__widgets[list_size].grid(row=0, column=list_size, stick='nsew')

    def get(self, index):
        return self.__widgets[index]

