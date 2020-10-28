import os
import time

from tkinter import *
import tkinter.ttk as ttk

from ClientEdit import *
from ClientInsert import *
from ClientView import *

class ClientList(Tk):
    def label_combo(self, text, frame=None):
        if frame == None:
            frame = self.__frame_border
        frame = Frame(frame)
        label = Label(frame, text=text)
        combobox = ttk.Combobox(frame, state='readonly')
        label.grid(row=0, column=0)
        combobox.grid(row=0, column=1)
        return [frame, combobox]

    def __init__(self, db):
        super().__init__()

        if os.name == 'nt':
            self.geometry("{}x{}+{}+{}".format(
                1008, 590,
                self.winfo_screenwidth()//2 - 1085//2,
                self.winfo_screenheight()//2 - 590//2
                )
            )
        else:
            self.geometry("{}x{}+{}+{}".format(
                1085, 590,
                self.winfo_screenwidth()//2 - 1085//2,
                self.winfo_screenheight()//2 - 590//2
                )
            )

        self.__db = db

        self.title("Listagem de Clientes")
        self.resizable(False, False)

        self.__frame_border = Frame(self)

        self.__label_pesquisa = Label(self.__frame_border, 
                text="Pesquisa:")
        self.__label_pesquisa.grid(row=0, column=0, stick='w')

        self.__entry_pesquisa = Entry(self.__frame_border)
        self.__entry_pesquisa.grid(row=1, column=0, stick='ew')
        self.__entry_pesquisa.focus()

        self.__frame_row2 = Frame(self.__frame_border)

        tmp = self.label_combo("Pesquisar por:", self.__frame_row2)
        self.__frame_selecao_pesquisa = tmp[0]
        self.__combo_selecao_pesquisa = tmp[1]
        self.__combo_selecao_pesquisa['values'] = ["Razão Social", "CNPJ"]
        self.__combo_selecao_pesquisa.current(0)
        self.__frame_selecao_pesquisa.grid(row=0, column=0, stick='w', pady=4)
        
        tmp = self.label_combo("Ordem:", self.__frame_row2)
        self.__frame_ordem = tmp[0]
        self.__combo_ordem = tmp[1]
        self.__combo_ordem['values'] = ["Crescente", "Decrescente"]
        self.__combo_ordem.current(0)
        self.__frame_ordem.grid(row=0, column=1, stick='w', pady=4)

        self.__button_filtrar = Button(self.__frame_row2, text='Filtrar',
                command=self.filter_client)
        self.__button_filtrar.grid(row=0, column=2, stick='e')
        
        self.__frame_row2.grid_columnconfigure(index=2, weight=1)

        self.__frame_row2.grid(row=2, column=0, stick='ew')

        self.__frame_row3 = Frame(self.__frame_border)

        campo_values = [
                "Razão Social",
                "Nome Fantasia",
                "CNPJ",
                "Inscrição Estadual",
                "Inscrição Municipal",
                "Logradouro",
                "Complemento",
                "Bairro",
                "Municipio",
                "UF",
                "CEP",
                "Telefone",
                "Celular",
                "E-mail",
                "URL"]
        
        tmp = self.label_combo("Campo 1:", self.__frame_row3)
        self.__frame_campo_1 = tmp[0]
        self.__combo_campo_1 = tmp[1]
        self.__combo_campo_1['values'] = campo_values
        self.__combo_campo_1.current(0)
        self.__frame_campo_1.grid(row=0, column=0, stick='ew', pady=4)
        
        tmp = self.label_combo("Campo 2:", self.__frame_row3)
        self.__frame_campo_2 = tmp[0]
        self.__combo_campo_2 = tmp[1]
        self.__combo_campo_2['values'] = campo_values
        self.__combo_campo_2.current(1)
        self.__frame_campo_2.grid(row=0, column=1, stick='ew', pady=4)

        tmp = self.label_combo("Campo 3:", self.__frame_row3)
        self.__frame_campo_3 = tmp[0]
        self.__combo_campo_3 = tmp[1]
        self.__combo_campo_3['values'] = campo_values
        self.__combo_campo_3.current(2)
        self.__frame_campo_3.grid(row=0, column=2, stick='ew', pady=4)

        tmp = self.label_combo("Campo 4:", self.__frame_row3)
        self.__frame_campo_4 = tmp[0]
        self.__combo_campo_4 = tmp[1]
        self.__combo_campo_4['values'] = campo_values
        self.__combo_campo_4.current(3)
        self.__frame_campo_4.grid(row=0, column=3, stick='ew', pady=4)
        
        tmp = self.label_combo("Página:", self.__frame_row3)
        self.__frame_pagina = tmp[0]
        self.__combo_pagina = tmp[1]
        self.__str_pagina = StringVar()
        self.__combo_pagina['textvariable'] = self.__str_pagina
        self.__combo_pagina['values'] = ["0"]
        self.__combo_pagina.current(0)
        self.__str_pagina.trace("w", self.__change_pagina)
        self.__frame_pagina.grid(row=0, column=4, stick='ew', pady=4)

        self.__frame_row3.grid(row=3, column=0)

        self.__tree = ttk.Treeview(self.__frame_border, height=21)
        self.__tree["columns"] = (1, 2, 3, 4)
        self.__tree["show"] = "headings"

        self.__tree.heading(1, text="Razão Social")
        self.__tree.heading(2, text="Nome Fantasia")
        self.__tree.heading(3, text="CNPJ")
        self.__tree.heading(4, text="Inscrição Estadual")

        self.__tree.column(1, width=200)
        self.__tree.column(2, width=200)
        self.__tree.column(3, width=200)
        self.__tree.column(4, width=200)
        self.__tree.grid(row=4, column=0, stick='ew')
        
        self.__tree.bind('<Button-1>', self.__handle_click)

        self.__frame_row5 = Frame(self.__frame_border)

        self.__button_inserir = Button(self.__frame_row5, text='Inserir',
                command=self.__insert_client)
        self.__button_editar = Button(self.__frame_row5, text='Editar',
                command=self.__edit_client)
        self.__button_consultar = Button(self.__frame_row5, text='Consultar',
                command=self.__view_client)
        self.__button_deletar = Button(self.__frame_row5, text='Deletar',
                command=self.__delete_client)
        
        self.__button_inserir.grid(row=0, column=0, stick='e', padx=4)
        self.__button_editar.grid(row=0, column=1, stick='e', padx=4)
        self.__button_consultar.grid(row=0, column=2, stick='e', padx=4)
        self.__button_deletar.grid(row=0, column=3, stick='e', padx=4)
        
        self.__frame_row5.grid_columnconfigure(index=0, weight=1)
        self.__frame_row5.grid_columnconfigure(index=1, weight=0)
        self.__frame_row5.grid_columnconfigure(index=2, weight=0)
        self.__frame_row5.grid_columnconfigure(index=3, weight=0)

        self.__frame_row5.grid(row=5, column=0, stick='ew', pady=4)

        self.__frame_border.grid(row=0, column=0,
                stick='ew', padx=10, pady=10)

        self.filter_client()

    def __handle_click(self, event):
            if self.__tree.identify_region(event.x, event.y) == "separator":
                return "break"

    def __combo_to_database(self, value):
        if value == "Razão Social":
            return "rsocial_cliente"

        if value == "Nome Fantasia":
            return "nfantasia_cliente"

        if value == "CNPJ":
            return "cnpj_cliente"

        if value == "Inscrição Estadual":
            return "iestadual_cliente"

        if value == "Inscrição Municipal":
            return "imunicipal_cliente"
        
        if value == "Logradouro":
            return "logradouro_cliente"
        
        if value == "Complemento":
            return "complemento_cliente"
        
        if value == "Bairro":
            return "bairro_cliente"
        
        if value == "CEP":
            return "cep_cliente"
        
        if value == "Celular":
            return "ncel_cliente"
        
        if value == "Telefone":
            return "numero_telefone"

        if value == "Municipio":
            return "nome_municipio"
        
        if value == "UF":
            return "nome_uf"
        
        if value == "URL":
            return "url_cliente"
        
        if value == "E-mail":
            return "email_cliente"

    def __format_result(self, name, value):
        if name == "cnpj_cliente":
            value = str(value)
            return value[:2] + "." + value[2:5] + "." + value[5:8] + "/" + value[8:12] + "." + value[12:15]
        if name == "iestadual_cliente":
            value = str(value)
            return value[:3] + "." + value[3:6] + "." + value[6:9] + "." + value[9:]
        if name == "imunicipal_cliente":
            value = str(value)
            return value[:1] + "." + value[1:4] + "." + value[4:7] + "-" + value[7:]
        if name == "cep_cliente":
            value = str(value)
            return value[:5] + "-" + value[5:]
        if name == "numero_telefone":
            tmp = ""
            print(value)
            for element in value:
                if (int(element["numero_telefone"]) != 0 and
                    int(element["ddd_telefone"]) != 0):
                    tmp += "(" + str(element["ddd_telefone"]) + ") " 
                    tmp += str(element["numero_telefone"])[:4] + "-"
                    tmp += str(element["numero_telefone"])[4:] + "; "
            if tmp[-1] == " " and tmp[-2] == ";":
                tmp = tmp[:-2]
            return tmp
        if name == "ncel_cliente":
            value = str(value)
            return value[:1] + " " + value[1:5] + "-" + value[5:]
        if name == "ddd_cel_cliente":
            value = str(value)
            return "(" + value[:2] + ") "
        value = str(value)
        return value

    def __general_client_query(self, field):
        campo_pesquisa = self.__combo_to_database(self.__combo_selecao_pesquisa.get())
        campo_ordem = "ASC" if self.__combo_ordem.get() == "Crescente" else "DESC"

        if len(self.__entry_pesquisa.get()) == 0:
            table = self.__db.select("CLIENTE", [field],
                    order_by=campo_pesquisa + " " + campo_ordem)
        else:
            table = self.__db.select("CLIENTE",
                    [field],
                    [campo_pesquisa],
                    [self.__entry_pesquisa.get()],
                    like=True,
                    order_by=campo_pesquisa + " " + campo_ordem)
        
        if (field == "cnpj_cliente" or field == "iestadual_cliente" or
            field == "imunicipal_cliente"):
            for i in range(len(table)):
                zeroes_to_add = 0
                if field == "cnpj_cliente":
                    if len(str(table[i][field])) < 14:
                        zeroes_to_add = 14 - len(str(table[i][field]))
                elif field == "iestadual_cliente":
                    if len(str(table[i][field])) < 12:
                        zeroes_to_add = 12 - len(str(table[i][field]))
                elif field == "imunicipal_cliente":
                    if len(str(table[i][field])) < 8:
                        zeroes_to_add = 8 - len(str(table[i][field]))
                if zeroes_to_add != 0:
                    for j in range(zeroes_to_add):
                        table[i][field] = "0" + str(table[i][field])

        tmp = []
        for i in range(len(table)):
            tmp.append(self.__format_result(field, table[i][field]))
        return tmp

    def __nome_municipio_query(self):
        id_list = self.__general_client_query('id_cliente')
        tmp = []
        for ident in id_list:
            id_municipio_cliente = str(self.__db.select("CLIENTE",
                    ["id_municipio_cliente"],
                    ["id_cliente"],
                    [str(ident)]
                    )[0]["id_municipio_cliente"])
            nome_municipio = str(self.__db.select("MUNICIPIO",
                    ["nome_municipio"],
                    ["id_municipio"],
                    [id_municipio_cliente])[0]["nome_municipio"])
            tmp.append(nome_municipio)
        return tmp
    
    def __nome_uf_query(self):
        id_list = self.__general_client_query('id_cliente')
        tmp = []
        for ident in id_list:
            id_municipio_cliente = str(self.__db.select("CLIENTE",
                    ["id_municipio_cliente"],
                    ["id_cliente"],
                    [str(ident)]
                    )[0]["id_municipio_cliente"])
            id_uf_municipio = str(self.__db.select("MUNICIPIO",
                    ["id_uf_municipio"],
                    ["id_municipio"],
                    [id_municipio_cliente])[0]["id_uf_municipio"])
            nome_uf = str(self.__db.select("UF",
                    ["nome_uf"],
                    ["id_uf"],
                    [id_uf_municipio])[0]["nome_uf"])
            tmp.append(nome_uf)
        return tmp
    
    def __numero_telefone_query(self):
        id_list = self.__general_client_query('id_cliente')
        tmp = []
        for ident in id_list:
            table = self.__db.select("TELEFONE",
                        ["ddd_telefone", "numero_telefone"],
                        ["id_cliente_telefone"],
                        [str(ident)])
            tmp.append(self.__format_result("numero_telefone", table))
        return tmp

    def __ncel_cliente_query(self):
        ddd = self.__general_client_query('ddd_cel_cliente')
        ncel = self.__general_client_query('ncel_cliente')

        tmp = []
        for i in range(len(ddd)):
            full = str(ddd[i]) + str(ncel[i])
            tmp.append(full)

        return tmp

    def __process_pag_number(self):
        pag_number = len(self.__table_cliente[0])//20
        tmp = []
        for i in range(pag_number+1):
            tmp.append(i)
        self.__combo_pagina['values'] = tmp
        self.__combo_pagina.current(0)

    def filter_client(self):
        for i in self.__tree.get_children():
            self.__tree.delete(i)

        self.__tree.heading(1, text=self.__combo_campo_1.get())
        self.__tree.heading(2, text=self.__combo_campo_2.get())
        self.__tree.heading(3, text=self.__combo_campo_3.get())
        self.__tree.heading(4, text=self.__combo_campo_4.get())

        self.__campo_db = ["id_cliente"]
        self.__campo_db.append(self.__combo_to_database(
            self.__combo_campo_1.get()))
        self.__campo_db.append(self.__combo_to_database(
            self.__combo_campo_2.get()))
        self.__campo_db.append(self.__combo_to_database(
            self.__combo_campo_3.get()))
        self.__campo_db.append(self.__combo_to_database(
            self.__combo_campo_4.get()))

        self.__table_cliente = []
        for campo in self.__campo_db:
            if campo == "nome_uf":
                self.__table_cliente.append(self.__nome_uf_query())
                continue
            elif campo == "nome_municipio":
                self.__table_cliente.append(self.__nome_municipio_query())
                continue
            elif campo == "numero_telefone":
                self.__table_cliente.append(self.__numero_telefone_query())
                continue
            elif campo == "ncel_cliente":
                self.__table_cliente.append(self.__ncel_cliente_query())
                continue
        
            self.__table_cliente.append(self.__general_client_query(campo))

        self.__process_pag_number()

        if len(self.__table_cliente[0]) == 0:
            self.__tree.insert('', 'end', values=[
                "Sem resultados.",
                "", "", ""])
            self.__button_consultar["state"] = "disabled"
            self.__button_editar["state"] = "disabled"
            self.__button_deletar["state"] = "disabled"
            child_id = self.__tree.get_children()[0]
            self.__tree.focus(child_id)
            self.__tree.selection_set(child_id)
            return

        self.__button_consultar["state"] = "normal"
        self.__button_editar["state"] = "normal"
        self.__button_deletar["state"] = "normal"

        child_id = self.__tree.get_children()[0]
        self.__tree.focus(child_id)
        self.__tree.selection_set(child_id)

    def __change_pagina(self, *args):
        for i in self.__tree.get_children():
            self.__tree.delete(i)

        values = ["", "", "", ""]
        actual_index = int(self.__combo_pagina.get())*20
        
        consult_size = len(self.__table_cliente[0])
        if actual_index + 20 > consult_size:
            final_index = consult_size
        else:
            final_index = actual_index + 20

        for i in range(actual_index, final_index):
            values[0] = self.__table_cliente[1][i]
            values[1] = self.__table_cliente[2][i]
            values[2] = self.__table_cliente[3][i]
            values[3] = self.__table_cliente[4][i]
            self.__tree.insert('', 'end', values=values)
        return

    def __get_client_id(self):
        selection = self.__tree.index(self.__tree.selection())
        return self.__table_cliente[0][selection]

    def __insert_client(self):
        instance_insert = ClientInsert(self.__db, self)
        self.filter_client()

    def __edit_client(self):
        instance_edit = ClientEdit(self.__db, self.__get_client_id(), self)
        self.filter_client()

    def __view_client(self):
        instance_view = ClientView(self.__db, self.__get_client_id(), self)
        self.filter_client()
    
    def __delete_client(self):
        if messagebox.askyesno("Questão", "Deseja excluir?"):
            self.__db.delete("TELEFONE",
                    ["id_cliente_telefone"], str(self.__get_client_id()))
            self.__db.delete("CLIENTE",
                    ["id_cliente"], str(self.__get_client_id()))
            self.filter_client()

