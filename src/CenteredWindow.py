from tkinter import *

class CenteredWindow(Tk):
    def __init__(self, width, height, title, resizeable=False):
        super().__init__()
        self.__width = width
        self.__height = height
        self.__center()
        self.title(title)
        self.resizable(resizeable, resizeable)

    def __center(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_right = int((screen_width/2) - (self.__width/2))
        position_down = int((screen_height/2) - (self.__height/2))
        self.geometry("{}x{}+{}+{}".format(self.__width, self.__height, position_right, position_down))

