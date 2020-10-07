from tkinter import *

class ColumnSplitter(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__widgets = []
        self.grid_rowconfigure(index=0, weight=1)

    def add(self, widget, weight=1, uniform='g1'):
        self.__widgets.append(widget)
        len_list = len(self.__widgets) - 1
        self.grid_columnconfigure(
                index=len_list, weight=weight, uniform=uniform)
        self.__widgets[len_list].grid(row=0, column=len_list, stick='nsew')

