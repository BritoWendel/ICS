from CenteredWindow import *
from ClientRegisterFrame import *

class ClientRegisterWindow(CenteredWindow):
    def __init__(self):
        super().__init__(width=800, height=450, title='Cadastro de cliente')
        app = ClientRegisterFrame(self)
        app.pack(fill='both', padx=10, pady=10)

