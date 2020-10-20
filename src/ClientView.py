from tkinter import messagebox

from ClientForm import ClientForm

class ClientView(ClientForm):
    def __init__(self, db, id_cliente, master):
        super().__init__(master)

        self.title('Consulta de Cliente')

        self._ClientForm__button_salvar.destroy()
        
        self._ClientForm__button_cancelar.config(
                command=self.__button_cancelar_action)

        table_cliente = db.select("CLIENTE", ["*"],
                ['id_cliente'], [str(id_cliente)])[0]

        table_municipio = db.select("MUNICIPIO",
                ["id_uf_municipio", "nome_municipio"],
                ["id_municipio"],
                [str(table_cliente["id_municipio_cliente"])])[0]

        table_uf = db.select("UF",
                ["nome_uf"],
                ["id_uf"],
                [str(table_municipio["id_uf_municipio"])])[0]

        table_telefone = db.select("TELEFONE",
                ["numero_telefone", "ddd_telefone"],
                ["id_cliente_telefone"],
                [str(id_cliente)])

        telefones = ""
        for telefone in table_telefone:
            if (telefone['ddd_telefone'] != 0 and
                    telefone['numero_telefone'] != 0):
                telefones += str(telefone['ddd_telefone'])
                telefones += str(telefone['numero_telefone'])

        self._ClientForm__str_rsocial.set(
                table_cliente['rsocial_cliente'])
        self._ClientForm__str_nfantasia.set(
                table_cliente['nfantasia_cliente'])
        self._ClientForm__tracer_cnpj.set(
                str(table_cliente['cnpj_cliente']))
        self._ClientForm__tracer_iestadual.set(
                str(table_cliente['iestadual_cliente']))
        self._ClientForm__tracer_imunicipal.set(
                str(table_cliente['imunicipal_cliente']))
        self._ClientForm__str_logradouro.set(
                table_cliente['logradouro_cliente'])
        self._ClientForm__str_complemento.set(
                table_cliente['complemento_cliente'])
        self._ClientForm__tracer_cep.set(
                str(table_cliente['cep_cliente']))
        self._ClientForm__tracer_telefone.set(
                telefones)

        celular = str(table_cliente['ddd_cel_cliente'])
        celular += str(table_cliente['ncel_cliente'])
        self._ClientForm__tracer_ncel.set(
                celular)
        
        self._ClientForm__str_bairro.set(
                table_cliente['bairro_cliente'])
        self._ClientForm__str_email.set(
                table_cliente['email_cliente'])
        self._ClientForm__str_url.set(
                table_cliente['url_cliente'])

        self._ClientForm__str_municipio.set(table_municipio["nome_municipio"])
        self._ClientForm__str_uf.set(table_uf["nome_uf"])
        
        self._ClientForm__int_whatsapp.set(table_cliente["whatsapp_cliente"])

        self._ClientForm__entry_rsocial.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_nfantasia.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_cnpj.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_iestadual.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_imunicipal.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_cep.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_ncel.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_bairro.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_email.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_url.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_complemento.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_logradouro.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__entry_telefone.config(state='disabled',
                disabledforeground='black')
        self._ClientForm__combo_municipio.config(state='disabled',
                foreground='black')
        self._ClientForm__combo_uf.config(state='disabled',
                foreground='black')
        self._ClientForm__check_whatsapp.config(state='disabled',
                disabledforeground='black')
        
        self._ClientForm__entry_rsocial.bind('<1>',
                self.__entry_rsocial_handle)
        self._ClientForm__entry_nfantasia.bind('<1>',
                self.__entry_nfantasia_handle)
        self._ClientForm__entry_cnpj.bind('<1>',
                self.__entry_cnpj_handle)
        self._ClientForm__entry_iestadual.bind('<1>',
                self.__entry_iestadual_handle)
        self._ClientForm__entry_imunicipal.bind('<1>',
                self.__entry_imunicipal_handle)
        self._ClientForm__entry_logradouro.bind('<1>',
                self.__entry_logradouro_handle)
        self._ClientForm__entry_complemento.bind('<1>',
                self.__entry_complemento_handle)
        self._ClientForm__entry_bairro.bind('<1>',
                self.__entry_bairro_handle)
        self._ClientForm__entry_email.bind('<1>',
                self.__entry_email_handle)
        self._ClientForm__entry_url.bind('<1>',
                self.__entry_url_handle)
        self._ClientForm__entry_cep.bind('<1>',
                self.__entry_cep_handle)
        self._ClientForm__entry_telefone.bind('<1>',
                self.__entry_telefone_handle)
        self._ClientForm__entry_ncel.bind('<1>',
                self.__entry_ncel_handle)
        self._ClientForm__combo_municipio.bind('<1>',
                self.__combo_municipio_handle)
        self._ClientForm__combo_uf.bind('<1>',
                self.__combo_uf_handle)

    def __button_cancelar_action(self):
        self.destroy()

    def __entry_handle_click(self, content, name):
        self.clipboard_clear()
        self.clipboard_append(content)
        messagebox.showinfo("Informação",
                "Campo '" + name + "' copiado para clipboard!")

    def __entry_rsocial_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_rsocial.get(),
                "Razão Social")

    def __entry_nfantasia_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_nfantasia.get(),
                "Nome Fantasia")
    
    def __entry_cnpj_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_cnpj.get(),
                "CNPJ")
    
    def __entry_iestadual_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_iestadual.get(),
                "Inscrição Estadual")
    
    def __entry_imunicipal_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_imunicipal.get(),
                "Inscrição Municipal")
    
    def __entry_logradouro_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_logradouro.get(),
                "Logradouro")
    
    def __entry_complemento_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_complemento.get(),
                "Complemento")
    
    def __entry_bairro_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_bairro.get(),
                "Bairro")
    
    def __entry_email_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_email.get(),
                "E-mail")
    
    def __entry_url_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_url.get(),
                "URL")
    
    def __entry_cep_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_cep.get(),
                "CEP")
    
    def __entry_telefone_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_telefone.get(),
                "Telefone")
    
    def __entry_ncel_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_ncel.get(),
                "Celular")
    
    def __combo_municipio_handle(self, event):
        self.__entry_handle_click(self._ClientForm__tracer_municipio.get(),
                "Municipio")
    
    def __combo_uf_handle(self, event):
        self.__entry_handle_click(self._ClientForm__str_uf.get(),
                "UF")

