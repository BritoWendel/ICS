from tkinter import *

from ClientListForm import ClientListForm
from CenteredWindow import CenteredWindow


class ClientList(CenteredWindow):
    def __init__(self):
        super().__init__(800, 487, 'Cadastro Cliente')

        self.__frame = Frame(self)
        self.__client_list_form = ClientListForm(self.__frame)
        self.__client_list_form.pack(fill='both')
        self.__frame.pack(fill='both', padx=10, pady=10)
