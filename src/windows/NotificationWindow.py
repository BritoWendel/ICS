from  CenteredWindow import CenteredWindow

from tkinter import *

class NotificationWindow(CenteredWindow):
    def __init__(self, message):
        super().__init__(600, 200, 'Notificação!')
        
        self.__frame = Frame(self)
        self.__label_message = Label(self, text = message)
        self.__label_message.pack()
        self.__button_ok = Button(self, text = 'OK')
        self.__button_ok.pack()


#remove the " ''' " of the lines below to see this winddows runnig
'''
instance_notification = NotificationWindow('UM ERRO OCORREU!')

instance_notification.mainloop()
'''
