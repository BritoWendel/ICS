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
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        positionRight = int((screenWidth/2) - (self.__width/2))
        positionDown = int((screenHeight/2) - (self.__height/2))
        self.geometry("{}x{}+{}+{}".format(self.__width, self.__height, positionRight, positionDown))

