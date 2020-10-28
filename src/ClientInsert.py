from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

from ClientForm import ClientForm

class ClientInsert(ClientForm):
    def __combo_uf_callback(self, *args):
        uf = self._ClientForm__combo_uf.get()
        id_uf = self.__db.select("UF", ['id_uf'],
                ['nome_uf'], [uf])[0]['id_uf']
        municipios = self.__db.select("MUNICIPIO", ['nome_municipio'],
                ['id_uf_municipio'], [str(id_uf)], 
                order_by="nome_municipio ASC")
        list_municipios = []
        for i in municipios:
            list_municipios.append(i['nome_municipio'])
        if len(list_municipios) == 0:
            list_municipios.append('')
        self.__list_municipios = list_municipios
        self._ClientForm__combo_municipio['values'] = list_municipios
        self._ClientForm__combo_municipio.current(0)

    def __init__(self, db, master):
        super().__init__(master)

        self.__db = db
        self.__list = master

        self.title('Cadastro de Cliente')

        self.protocol('WM_DELETE_WINDOW', self.__button_cancelar_action)
        self._ClientForm__button_salvar.config(
                command=self.__button_salvar_action)
        self._ClientForm__button_cancelar.config(
                command=self.__button_cancelar_action)
        
        self._ClientForm__entry_cnpj.bind('<Control-c>',
                self.__clipboard_copy_cnpj)
        self._ClientForm__entry_iestadual.bind('<Control-c>',
                self.__clipboard_copy_iestadual)
        self._ClientForm__entry_imunicipal.bind('<Control-c>',
                self.__clipboard_copy_imunicipal)
        self._ClientForm__entry_cep.bind('<Control-c>',
                self.__clipboard_copy_cep)
        self._ClientForm__entry_telefone.bind('<Control-c>',
                self.__clipboard_copy_telefone)
        self._ClientForm__entry_ncel.bind('<Control-c>',
                self.__clipboard_copy_ncel)

        self._ClientForm__entry_cnpj.bind('<Control-v>',
                self.__clipboard_paste_cnpj)
        self._ClientForm__entry_iestadual.bind('<Control-v>',
                self.__clipboard_paste_iestadual)
        self._ClientForm__entry_imunicipal.bind('<Control-v>',
                self.__clipboard_paste_imunicipal)
        self._ClientForm__entry_cep.bind('<Control-v>',
                self.__clipboard_paste_cep)
        self._ClientForm__entry_telefone.bind('<Control-v>',
                self.__clipboard_paste_telefone)
        self._ClientForm__entry_ncel.bind('<Control-v>',
                self.__clipboard_paste_ncel)
        
        list_ufs = []
        for i in db.select("UF", [ 'nome_uf' ], order_by='nome_uf ASC'):
            list_ufs.append(i['nome_uf'])
        self.__list_ufs = list_ufs
        self._ClientForm__combo_uf.config(values=list_ufs)
        self._ClientForm__str_uf.trace("w", self.__combo_uf_callback)

        self._ClientForm__entry_rsocial.focus()
        old = self._ClientForm__str_rsocial.get()
        self._ClientForm__combo_uf.current(24)

    def __clipboard_copy_cnpj(self, event):
        self.clipboard_clear()
        self.clipboard_append(
                self._ClientForm__tracer_cnpj.get(
                    self._ClientForm__entry_cnpj.selection_get()
                    )
                )
        return 'break'
    
    def __clipboard_copy_iestadual(self, event):
        self.clipboard_clear()
        self.clipboard_append(
                self._ClientForm__tracer_iestadual.get(
                    self._ClientForm__entry_iestadual.selection_get()
                    )
                )
        return 'break'
    
    def __clipboard_copy_imunicipal(self, event):
        self.clipboard_clear()
        self.clipboard_append(
                self._ClientForm__tracer_imunicipal.get(
                    self._ClientForm__entry_imunicipal.selection_get()
                    )
                )
        return 'break'
    
    def __clipboard_copy_cep(self, event):
        self.clipboard_clear()
        self.clipboard_append(
                self._ClientForm__tracer_cep.get(
                    self._ClientForm__entry_cep.selection_get()
                    )
                )
        return 'break'
    
    def __clipboard_copy_telefone(self, event):
        self.clipboard_clear()
        self.clipboard_append(
                self._ClientForm__tracer_telefone.get(
                    self._ClientForm__entry_telefone.selection_get()
                    )
                )
        return 'break'
    
    def __clipboard_copy_ncel(self, event):
        self.clipboard_clear()
        self.clipboard_append(
                self._ClientForm__tracer_ncel.get(
                    self._ClientForm__entry_ncel.selection_get()
                    )
                )
        return 'break'

    def __clipboard_paste_cnpj(self, event):
        self._ClientForm__tracer_cnpj.set(self.clipboard_get())
        return 'break'

    def __clipboard_paste_iestadual(self, event):
        self._ClientForm__tracer_iestadual.set(self.clipboard_get())
        return 'break'

    def __clipboard_paste_imunicipal(self, event):
        self._ClientForm__tracer_imunicipal.set(self.clipboard_get())
        return 'break'
    
    def __clipboard_paste_cep(self, event):
        self._ClientForm__tracer_cep.set(self.clipboard_get())
        return 'break'
    
    def __clipboard_paste_telefone(self, event):
        self._ClientForm__tracer_telefone.set(self.clipboard_get())
        return 'break'
    
    def __clipboard_paste_ncel(self, event):
        self._ClientForm__tracer_ncel.set(self.clipboard_get())
        return 'break'
    
    def __weight(self, weight, value):
        return sum(int(value[i]) * weight[i] for i in range(len(weight))) % 11

    def __button_salvar_action(self):
        data = self.__data_validation()
        if data == None:
            return
        self.__database_insert(data)
        self.__list.filter_client()

    def __data_validation(self):
        error = False

        rsocial = self._ClientForm__str_rsocial.get()

        if rsocial == "":
            self._ClientForm__label_rsocial.config(fg="red")
            error = True
        else:
            self._ClientForm__label_rsocial.config(fg="black")

        nfantasia = self._ClientForm__str_nfantasia.get()

        if nfantasia == "":
            self._ClientForm__label_nfantasia.config(fg="red")
            error = True
        else:
            self._ClientForm__label_nfantasia.config(fg="black")

        cnpj = self._ClientForm__tracer_cnpj.get()
        
        z = self.__weight
        sub11 = lambda a: str(0 if a < 2 else 11 - a)

        if cnpj == "" or len(cnpj) < 14:
            self._ClientForm__label_cnpj.config(fg="red")
            error = True
        else:
            w = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            if cnpj[12:] == sub11(z(w[1:], cnpj)) + sub11(z(w, cnpj)):
                self._ClientForm__label_cnpj.config(fg="black")
            else:
                self._ClientForm__label_cnpj.config(fg="red")
                error = True

        iestadual = self._ClientForm__tracer_iestadual.get()

        if iestadual == "" or len(iestadual) < 12:
            self._ClientForm__label_iestadual.config(fg="red")
            error = True
        else:
            w = [1, 3, 4, 5, 6, 7, 8, 10]
            w1 = [3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            verify = lambda a: str(z(a, iestadual))[-1] == iestadual[len(a)]
            if verify(w) and verify(w1):
                self._ClientForm__label_iestadual.config(fg="black")
            else:
                self._ClientForm__label_iestadual.config(fg="red")
                error = True

        imunicipal = self._ClientForm__tracer_imunicipal.get()

        if imunicipal == "" or len(imunicipal) < 8:
            self._ClientForm__label_imunicipal.config(fg="red")
            error = True
        else:
            w = [2, 3, 4, 5, 6, 7, 8]
            if imunicipal[-1] == sub11(z(w, imunicipal)):
                self._ClientForm__label_imunicipal.config(fg="black")
            else:
                self._ClientForm__label_imunicipal.config(fg="red")
                error = True

        logradouro = self._ClientForm__str_logradouro.get()

        if logradouro == "":
            self._ClientForm__label_logradouro.config(fg="red")
            error = True
        else:
            self._ClientForm__label_logradouro.config(fg="black")

        complemento = self._ClientForm__str_complemento.get()

        if complemento == "":
            self._ClientForm__label_complemento.config(fg="red")
            error = True
        else:
            self._ClientForm__label_complemento.config(fg="black")

        bairro = self._ClientForm__str_bairro.get()

        if bairro == "":
            self._ClientForm__label_bairro.config(fg="red")
            error = True
        else:
            self._ClientForm__label_bairro.config(fg="black")

        municipio = self._ClientForm__str_municipio.get()

        if municipio == "":
            self._ClientForm__label_municipio.config(fg="red")
            error = True
        else:
            self._ClientForm__label_municipio.config(fg="black")

        uf = self._ClientForm__str_uf.get()

        if uf == "":
            self._ClientForm__label_uf.config(fg="red")
            error = True
        else:
            self._ClientForm__label_uf.config(fg="black")

        cep = self._ClientForm__tracer_cep.get()

        if cep == "" or len(cep) < 8:
            self._ClientForm__label_cep.config(fg="red")
            error = True
        else:
            self._ClientForm__label_cep.config(fg="black")

        telefone = self._ClientForm__tracer_telefone.get()
        len_telefone = len(telefone)
            
        allowed_ddds = ["11", "12", "13", "14", "15", "16", "17", 18, "19"]
        first_digit = ["2", "3", "4", "5"]

        if (telefone == "" or len_telefone < 10 or
        (len_telefone > 10 and len_telefone < 20) or
        (len_telefone > 20 and len_telefone < 30) or
        telefone[:2] not in allowed_ddds or
        telefone[2:3] not in first_digit or
        telefone[10:12] not in allowed_ddds or
        telefone[12:13] not in first_digit or
        telefone[20:22] not in allowed_ddds or
        telefone[22:23] not in first_digit):
            self._ClientForm__label_telefone.config(fg="red")
            error = True
        else:
            self.__ddd_telefone3 = "00"
            self.__number_telefone3 = "00000000"
            self.__ddd_telefone2 = "00"
            self.__number_telefone2 = "00000000"
            
            if len_telefone == 20:
                self.__ddd_telefone2 = telefone[10:12]
                self.__number_telefone2 = telefone[12:20]

            if len_telefone == 30:
                self.__ddd_telefone3 = telefone[20:22]
                self.__number_telefone3 = telefone[22:30]
                self.__ddd_telefone2 = telefone[10:12]
                self.__number_telefone2 = telefone[12:20]
            
            self.__ddd_telefone = telefone[:2]
            self.__number_telefone = telefone[2:10]
            self._ClientForm__label_telefone.config(fg="black")

        ncel = self._ClientForm__tracer_ncel.get()
        
        first_digit = ["6", "7", "8", "9"]

        if (ncel == "" or len(ncel) < 11 or
            ncel[:2] not in allowed_ddds or
            ncel[3:4] not in first_digit):
            self._ClientForm__label_ncel.config(fg="red")
            error = True
        else:
            self._ClientForm__label_ncel.config(fg="black")

        whatsapp = str(self._ClientForm__int_whatsapp.get())

        email = self._ClientForm__str_email.get()
        
        domain_br = [".com.br", ".net.br", ".edu.br"]
        domain = [".com", ".net", ".edu"]

        pos = 0
        for char in email:
            pos += 1
            if char == "@":
                break

        pos_dominio = 0
        for char in email[pos:]:
            pos_dominio += 1
            if char == ".":
                break

        count = 0
        for char in email:
            if char == "@":
                count += 1

        if (email == "" or pos < 2 or pos_dominio < 3 or count > 1 or
            (email[len(email)-4:] not in domain and
             email[len(email)-7:] not in domain_br)):
            self._ClientForm__label_email.config(fg="red")
            error = True
        else:
            self._ClientForm__label_email.config(fg="black")

        url = self._ClientForm__str_url.get()

        pos = 0
        for char in url[4:]:
            pos += 1
            if char == ".":
                break

        if (url == "" or pos < 3 or
            url[3:] in domain or
            url[3:] in domain_br or
            url[:4] != "www." or
            (url[len(url)-4:] not in domain and
             url[len(url)-7:] not in domain_br)):
            self._ClientForm__label_url.config(fg="red")
            error = True
        else:
            self._ClientForm__label_url.config(fg="black")

        if error:
            return None

        return [rsocial, nfantasia, cnpj, iestadual, imunicipal, logradouro,
                complemento, bairro, municipio, uf, cep, telefone, ncel, 
                whatsapp, email, url] 

    def __database_insert(self, data):
        rsocial = data[0]
        nfantasia = data[1]
        cnpj = data[2]
        iestadual = data[3]
        imunicipal = data[4]
        logradouro = data[5]
        complemento = data[6]
        bairro = data[7]
        municipio = data[8]
        uf = data[9]
        cep = data[10]
        telefone = data[11]
        ncel = data[12]
        whatsapp = data[13]
        email = data[14]
        url = data[15]

        uf_id = str(self.__db.select("UF",
                ['id_uf'], ['nome_uf'], [uf])[0]['id_uf'])

        municipio_id = self.__db.select("MUNICIPIO",
                ['id_municipio'],
                ['nome_municipio', 'id_uf_municipio'],
                [municipio, uf_id])

        if len(municipio_id) == 0:
            self.__db.insert("MUNICIPIO", 
                    ['nome_municipio', 'id_uf_municipio'],
                    [municipio, uf_id])
            municipio_id = str(self.__db.last_insert_id())
        else:
            municipio_id = str(municipio_id[0]['id_municipio'])

        self.__db.insert("CLIENTE",
                ['bairro_cliente',
                 'cep_cliente',
                 'rsocial_cliente',
                 'ncel_cliente',
                 'ddd_cel_cliente',
                 'nfantasia_cliente',
                 'whatsapp_cliente',
                 'cnpj_cliente',
                 'iestadual_cliente',
                 'imunicipal_cliente',
                 'logradouro_cliente',
                 'email_cliente',
                 'complemento_cliente',
                 'url_cliente',
                 'id_municipio_cliente'],
                [bairro,
                 cep,
                 rsocial,
                 ncel[2:],
                 ncel[:2],
                 nfantasia,
                 whatsapp,
                 cnpj,
                 iestadual,
                 imunicipal,
                 logradouro,
                 email,
                 complemento,
                 url,
                 municipio_id])

        cliente_id = self.__db.last_insert_id()[0]['LAST_INSERT_ID()']

        self.__db.insert("TELEFONE",
                ["ddd_telefone",
                 "numero_telefone",
                 "id_cliente_telefone"],
                [self.__ddd_telefone,
                 self.__number_telefone,
                 str(cliente_id)])

        self.__db.insert("TELEFONE",
                ["ddd_telefone",
                 "numero_telefone",
                 "id_cliente_telefone"],
                [self.__ddd_telefone2,
                 self.__number_telefone2,
                 str(cliente_id)])

        self.__db.insert("TELEFONE",
                ["ddd_telefone",
                 "numero_telefone",
                 "id_cliente_telefone"],
                [self.__ddd_telefone3,
                 self.__number_telefone3,
                 str(cliente_id)])

        messagebox.showinfo("Informação", "Dados adicionados!", parent=self)

        self.destroy()

    def __button_cancelar_action(self):
        if messagebox.askyesno("Alerta", "Realmente deseja sair?", parent=self):
            self.destroy()
