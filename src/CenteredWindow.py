from tkinter import *

class CenteredWindow(Tk):
    def __init__(self, width, height, title):
        super().__init__()
        self.geometry("{}x{}+{}+{}".format(
            width, height,
            self.winfo_screenwidth()//2 - width//2,
            self.winfo_screenheight()//2 - height//2
            )
        )
        self.title(title)
        self.resizable(False, False)
