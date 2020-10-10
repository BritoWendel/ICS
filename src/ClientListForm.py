from tkinter import *
import tkinter.ttk as ttk

class ClientListForm(Frame):
    def __init__(self, master):
        super().__init__(master)

        pad = 4

        self.__tree = ttk.Treeview(self)
        self.__tree["columns"] = (1, 2, 3, 4)
        self.__tree["show"] = "headings"

        self.__tree.heading(1, text="ID")
        self.__tree.heading(2, text="Razão Social")
        self.__tree.heading(3, text="CNPJ")
        self.__tree.heading(4, text="Inscrição Estadual")

        self.__tree.column(1, width=50)
        self.__tree.column(2, width=200)
        self.__tree.column(3, width=200)
        self.__tree.column(4, width=200)

        self.__label_pesquisar = Label(self, text="Pesquisar:")
        self.__entry_pesquisar = Entry(self)
        self.__button_ok = Button(self, text='OK')
        self.__button_editar = Button(self, text='Editar')
        self.__button_consultar = Button(self, text='Consultar')
        self.__button_inserir = Button(self, text='Inserir')

        self.__label_pesquisar.grid(row=0, column=0, stick='w')
        self.__entry_pesquisar.grid(row=1, column=0, stick='we', columnspan=3)
        self.__button_ok.grid(row=1, column=3, stick='we', padx=pad, pady=pad)
        self.__button_editar.grid(row=2, column=1, stick='we', padx=pad, pady=pad)
        self.__button_consultar.grid(row=2, column=2, stick='we', padx=pad, pady=pad)
        self.__button_inserir.grid(row=2, column=3, stick='we', padx=pad, pady=pad)
        self.__tree.grid(row=3, column=0, stick='we', columnspan=4)

        def handle_click(event, treeview):
            if treeview.identify_region(event.x, event.y) == "separator":
                return "break"

        self.__tree.bind('<Button-1>', lambda event: handle_click(event, self.__tree))

        self.grid_columnconfigure(index=0, weight=4)

