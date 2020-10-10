from tkinter import *
import tkinter.ttk as ttk

class ClientList(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("{}x{}+{}+{}".format(
            800, 487,
            self.winfo_screenwidth()//2 - 800//2,
            self.winfo_screenheight()//2 - 487//2
            )
        )
        self.title("Listagem de Clientes")
        self.resizable(False, False)

        self.__frame_border = Frame(self)

        pad = 4

        self.__tree = ttk.Treeview(self.__frame_border)
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

        self.__label_pesquisar = Label(self.__frame_border, text="Pesquisar:")
        self.__entry_pesquisar = Entry(self.__frame_border)
        self.__button_ok = Button(self.__frame_border, text='OK')
        self.__button_editar = Button(self.__frame_border, text='Editar')
        self.__button_consultar = Button(self.__frame_border, text='Consultar')
        self.__button_inserir = Button(self.__frame_border, text='Inserir')

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

        self.__frame_border.grid_columnconfigure(index=0, weight=4)
        
        self.grid_columnconfigure(index=0, minsize=1, weight=1)

        self.__frame_border.grid(row=0, column=0,
                stick='ew', padx=10, pady=10)

