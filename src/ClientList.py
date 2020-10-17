from tkinter import *
import tkinter.ttk as ttk

class ClientList(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("{}x{}+{}+{}".format(
            1050, 487,
            self.winfo_screenwidth()//2 - 1050//2,
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

        self.__label_pesquisa = Label(self.__frame_border, text="Pesquisa:")
        self.__entry_pesquisa = Entry(self.__frame_border)
        self.__label_selecao_pesquisa = Label(self.__frame_border, text="Pesquisar por:")
        self.__combobox_selecao_pesquisa = ttk.Combobox(self.__frame_border)
        self.__label_ordem = Label(self.__frame_border, text="Ordem:")
        self.__combobox_ordem = ttk.Combobox(self.__frame_border)
        self.__label_campo_1 = Label(self.__frame_border, text="Campo 1:")
        self.__combobox_campo_1 = ttk.Combobox(self.__frame_border)
        self.__label_campo_2 = Label(self.__frame_border, text="Campo 2:")
        self.__combobox_campo_2 = ttk.Combobox(self.__frame_border)
        self.__label_campo_3 = Label(self.__frame_border, text="Campo 3:")
        self.__combobox_campo_3 = ttk.Combobox(self.__frame_border)
        self.__label_campo_4 = Label(self.__frame_border, text="Campo 4:")
        self.__combobox_campo_4 = ttk.Combobox(self.__frame_border)
        self.__label_pagina = Label(self.__frame_border, text="Página:")
        self.__combobox_pagina = ttk.Combobox(self.__frame_border, width=3)
        self.__button_filtrar = Button(self.__frame_border, text='Filtrar')
        self.__button_inserir = Button(self.__frame_border, text='Inserir')
        self.__button_editar = Button(self.__frame_border, text='Editar')
        self.__button_deletar = Button(self.__frame_border, text='Deletar')

        self.__label_pesquisa.grid(row=0, column=0, stick='w')
        self.__entry_pesquisa.grid(row=1, column=0, stick='we', columnspan=10)
        self.__label_selecao_pesquisa.grid(row=2, column=0, stick='w', pady=pad)
        self.__combobox_selecao_pesquisa.grid(row=2, column=1, stick='w', pady=pad)
        self.__label_ordem.grid(row=2, column=2, stick='w', pady=pad)
        self.__combobox_ordem.grid(row=2, column=3, stick='w', pady=pad)
        self.__label_campo_1.grid(row=3, column=0, stick='w', pady=pad)
        self.__combobox_campo_1.grid(row=3, column=1, stick='w', pady=pad)
        self.__label_campo_2.grid(row=3, column=2, stick='w', pady=pad)
        self.__combobox_campo_2.grid(row=3, column=3, stick='w', pady=pad)
        self.__label_campo_3.grid(row=3, column=4, stick='w', pady=pad)
        self.__combobox_campo_3.grid(row=3, column=5, stick='w', pady=pad)
        self.__label_campo_4.grid(row=3, column=6, stick='w', pady=pad)
        self.__combobox_campo_4.grid(row=3, column=7, stick='w', pady=pad)
        self.__label_pagina.grid(row=3, column=8, stick='w', pady=pad)
        self.__combobox_pagina.grid(row=3, column=9, stick='w', pady=pad)
        self.__button_filtrar.grid(row=2, column=9, stick='we', padx=pad, pady=pad)
        self.__button_inserir.grid(row=5, column=7, stick='we', padx=pad, pady=pad)
        self.__button_editar.grid(row=5, column=8, stick='we', padx=pad, pady=pad)
        self.__button_deletar.grid(row=5, column=9, stick='we', padx=pad, pady=pad)
        self.__tree.grid(row=4, column=0, stick='we', columnspan=10)

        def handle_click(event, treeview):
            if treeview.identify_region(event.x, event.y) == "separator":
                return "break"

        self.__tree.bind('<Button-1>', lambda event: handle_click(event, self.__tree))

        self.__frame_border.grid_columnconfigure(index=0, weight=4)
        
        self.grid_columnconfigure(index=0, minsize=1, weight=1)

        self.__frame_border.grid(row=0, column=0,
                stick='ew', padx=10, pady=10)

