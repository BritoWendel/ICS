from tkinter import *

from widgets.Checkbox import *
from widgets.EEntry import *

class ClientForm(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.__label_rsocial = Label(self, text='Razão Social')
        self.__label_nfantasia = Label(self, text='Nome Fantasia')
        self.__label_cnpj = Label(self, text='CNPJ')
        self.__label_iestadual = Label(self, text='Inscrição Estadual')
        self.__label_imunicipal = Label(self, text='Inscrição Municipal')
        self.__label_logradouro = Label(self, text='Logradouro')
        self.__label_complemento = Label(self, text='Complemento')
        self.__label_bairro = Label(self, text='Bairro')
        self.__label_municipio = Label(self, text='Municipio')
        self.__label_uf = Label(self, text='UF')
        self.__label_cep = Label(self, text='CEP')
        self.__label_telefone = Label(self, text='Telefone')
        self.__label_ncel = Label(self, text='Celular')
        self.__label_email = Label(self, text='E-mail')
        self.__label_url = Label(self, text='URL')

        self.__entry_rsocial = EEntry(self, ALPHANUMERIC + SPACE, 255)
        self.__entry_nfantasia = EEntry(self, ALPHANUMERIC + SPACE, 255)
        self.__entry_cnpj = EEntry(self, NUMERIC, 14)
        self.__entry_iestadual = EEntry(self, NUMERIC, 12)
        self.__entry_imunicipal = EEntry(self, NUMERIC, 8)
        self.__entry_logradouro = EEntry(self, ALPHANUMERIC + SPACE, 255)
        self.__entry_complemento = EEntry(self, ALPHANUMERIC + SPACE, 255)
        self.__entry_bairro = EEntry(self, ALPHABET + SPACE, 255)
        self.__entry_municipio = EEntry(self, ALPHABET + SPACE, 255)
        self.__entry_uf = EEntry(self, ALPHABET + SPACE, 255)
        self.__entry_cep = EEntry(self, NUMERIC, 8)
        self.__entry_telefone = EEntry(self, NUMERIC, 10)
        self.__entry_ncel = EEntry(self, NUMERIC, 11)
        
        self.__check_whatsapp = Checkbox(self, 'WhatsApp?')

        self.__entry_email = EEntry(self, ALPHANUMERIC + "_@-.", 255)
        self.__entry_url = EEntry(self, ALPHANUMERIC + "_-./", 255)

        self.__button_salvar = Button(
                self, text="Salvar", command=self.__entry_telefone.get_raw)
        self.__button_cancelar = Button(
                self, text="Cancelar", command=self.destroy)
        
        self.__entry_cep.rule_add(5, '-')

        self.__entry_cnpj.rule_add(2, '.')
        self.__entry_cnpj.rule_add(5, '.')
        self.__entry_cnpj.rule_add(8, '/')
        self.__entry_cnpj.rule_add(12, '-')

        self.__entry_iestadual.rule_add(3, '.')
        self.__entry_iestadual.rule_add(6, '.')
        self.__entry_iestadual.rule_add(9, '.')
        
        self.__entry_imunicipal.rule_add(1, '.')
        self.__entry_imunicipal.rule_add(4, '.')
        self.__entry_imunicipal.rule_add(7, '-')
        
        self.__entry_telefone.rule_add(0, '(')
        self.__entry_telefone.rule_add(2, ') ')
        self.__entry_telefone.rule_add(7, '-')
        
        self.__entry_ncel.rule_add(0, '(')
        self.__entry_ncel.rule_add(2, ') ')
        self.__entry_ncel.rule_add(4, ' ')
        self.__entry_ncel.rule_add(8, '-')
        
        self.grid_columnconfigure(index=0, minsize=1, weight=5)
        self.grid_columnconfigure(index=1, minsize=1, weight=1)
        self.grid_columnconfigure(index=2, minsize=1, weight=1)
       
        self.__label_rsocial.grid(row=0, column=0, stick='w')
        self.__label_nfantasia.grid(row=2, column=0, stick='w')
        self.__label_cnpj.grid(row=2, column=1, stick='w')
        self.__label_iestadual.grid(row=4, column=0, stick='w')  
        self.__label_imunicipal.grid(row=4, column=1, stick='w')
        self.__label_logradouro.grid(row=6, column=0, stick='w')  
        self.__label_complemento.grid(row=8, column=0, stick='w')
        self.__label_bairro.grid(row=8, column=1, stick='w')
        self.__label_municipio.grid(row=10, column=0, stick='w')
        self.__label_uf.grid(row=10, column=1, stick='w')
        self.__label_cep.grid(row=10, column=3, stick='w')    
        self.__label_telefone.grid(row=12, column=0, stick='w')   
        self.__label_ncel.grid(row=12, column=1, stick='w')
        self.__label_email.grid(row=14, column=0, stick='w')   
        self.__label_url.grid(row=16, column=0, stick='w')

        self.__entry_rsocial.grid(row=1, column=0, columnspan=6, stick='ew', pady=3)
        self.__entry_nfantasia.grid(row=3, column=0, stick='ew', pady=3)
        self.__entry_cnpj.grid(row=3, column=1, columnspan=5, stick='ew', pady=3)
        self.__entry_iestadual.grid(row=5, column=0, stick='ew', pady=3)
        self.__entry_imunicipal.grid(row=5, column=1, columnspan=5, stick='ew', pady=3)
        self.__entry_logradouro.grid(row=7, column=0, columnspan=6, stick='ew', pady=3)
        self.__entry_complemento.grid(row=9, column=0, stick='ew', pady=3)
        self.__entry_bairro.grid(row=9, column=1, columnspan=5, stick='ew', pady=3)
        self.__entry_municipio.grid(row=11, column=0, stick='ew', pady=3)
        self.__entry_uf.grid(row=11, column=1, columnspan=2, stick='ew', pady=3)
        self.__entry_cep.grid(row=11, column=3, columnspan=4, stick='ew', pady=3)
        self.__entry_telefone.grid(row=13, column=0, stick='ew', pady=3)
        self.__entry_ncel.grid(row=13, column=1, columnspan=4, stick='ew', pady=3)
        self.__check_whatsapp.grid(row=13, column=5, stick='nsew', pady=3)
        self.__entry_email.grid(row=15, column=0, columnspan=6, stick='ew', pady=3)
        self.__entry_url.grid(row=17, column=0, columnspan=6, stick='ew', pady=3)

        self.__button_salvar.grid(row=18, column=4, stick='e', pady=3)
        self.__button_cancelar.grid(row=18, column=5, stick='e', pady=3)

    def get_rsocial(self):
        self.__entry_rsocial.get_raw()

    def get_nfantasia(self):
        self.__entry_nfantasia.get_raw()

    def get_cnpj(self):
        self.__entry_cnpj.get_raw()

    def get_iestadual(self):
        self.__entry_iestadual.get_raw()

    def get_imunicipal(self):
        self.__entry_imunicipal.get_raw()

    def get_logradouro(self):
        self.__entry_logradouro.get_raw()

    def get_complemento(self):
        self.__entry_complemento.get_raw()

    def get_bairro(self):
        self.__entry_bairro.get_raw()

    def get_municipio(self):
        self.__entry_municipio.get_raw()

    def get_uf(self):
        self.__entry_uf.get_raw()

    def get_cep(self):
        self.__entry_cep.get_raw()

    def get_telefone(self):
        self.__entry_telefone.get_raw()

    def get_celular(self):
        self.__entry_celular.get_raw()

    def get_email(self):
        self.__entry_email.get_raw()

    def get_url(self):
        self.__entry_url.get_raw()
    
    def set_rsocial(self, value):
        self.__entry_rsocial.set_raw(value)

    def set_nfantasia(self, value):
        self.__entry_nfantasia.set_raw(value)

    def set_cnpj(self, value):
        self.__entry_cnpj.set_raw(value)

    def set_iestadual(self, value):
        self.__entry_iestadual.set_raw(value)

    def set_imunicipal(self, value):
        self.__entry_imunicipal.set_raw(value)

    def set_logradouro(self, value):
        self.__entry_logradouro.set_raw(value)

    def set_complemento(self, value):
        self.__entry_complemento.set_raw(value)

    def set_bairro(self, value):
        self.__entry_bairro.set_raw(value)

    def set_municipio(self, value):
        self.__entry_municipio.set_raw(value)

    def set_uf(self, value):
        self.__entry_uf.set_raw(value)

    def set_cep(self, value):
        self.__entry_cep.set_raw(value)

    def set_telefone(self, value):
        self.__entry_telefone.set_raw(value)

    def set_celular(self, value):
        self.__entry_celular.set_raw(value)

    def set_email(self, value):
        self.__entry_email.set_raw(value)

    def set_url(self, value):
        self.__entry_url.set_raw(value)
