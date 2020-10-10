from  CenteredWindow import CenteredWindow

from tkinter import *

class NotificationWindow(CenteredWindow):
    def __init__(self, message):
        super().__init__(600, 200, 'Notificação!')
        #----------------------widgets--------------------
        self.__label_message = Label(self, text = message, pady = 20)
        self.__button_cancel = Button(self, text = 'Cancelar')
        self.__button_ok = Button(self, text = 'OK')

        #------------------grid configure-----------------
        self.grid_columnconfigure(index=0, minsize=1, weight=1)
        self.grid_columnconfigure(index=1, minsize=1, weight=1)
        self.grid_columnconfigure(index=2, minsize=1, weight=1)
        self.grid_rowconfigure(index=0, minsize=1, weight=1)
        self.grid_rowconfigure(index=1, minsize=1, weight=1)
        self.grid_rowconfigure(index=2, minsize=1, weight=1)

        #----------------------layout---------------------
        self.__label_message.grid(row=0, column=0, columnspan=3)
        self.__button_cancel.grid(row=2, column=0)
        self.__button_ok.grid(row=2, column=2)


#remove the " ''' " of the lines below to see this winddows runnig

instance_notification = NotificationWindow('UM ERRO OCORREU!')

instance_notification.mainloop()

