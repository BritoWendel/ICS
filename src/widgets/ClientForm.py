from tkinter import *

from widgets.Checkbox import *
from widgets.ColumnSplitter import *
from widgets.LabelEntry import *

class ClientForm(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.__frame0 = ColumnSplitter(self)
        self.__frame1 = ColumnSplitter(self)
        self.__frame2 = ColumnSplitter(self)
        self.__frame3 = ColumnSplitter(self)
        self.__frame4 = ColumnSplitter(self)

        self.__frame3_sub = ColumnSplitter(self.__frame3)
        self.__frame4_sub = ColumnSplitter(self.__frame4)

        self.__entry_rsocial     = LabelEntry(
                self, 'Razão Social', ALPHANUMERIC + SPACE, 255)
        self.__entry_nfantasia   = LabelEntry(
                self.__frame0, 'Nome Fantasia', ALPHANUMERIC + SPACE, 255)
        self.__entry_cnpj        = LabelEntry(
                self.__frame0, 'CNPJ', NUMERIC, 14)
        self.__entry_iestadual   = LabelEntry(
                self.__frame1, 'Inscrição Estadual', NUMERIC, 12)
        self.__entry_imunicipal  = LabelEntry(
                self.__frame1, 'Inscrição Municipal', NUMERIC, 8)
        self.__entry_logradouro  = LabelEntry(
                self, 'Logradouro', ALPHANUMERIC + SPACE, 255)
        self.__entry_complemento = LabelEntry(
                self.__frame2, 'Complemento', ALPHANUMERIC + SPACE, 255)
        self.__entry_bairro      = LabelEntry(
                self.__frame2, 'Bairro', ALPHABET + SPACE, 255)
        self.__entry_municipio   = LabelEntry(
                self.__frame3, 'Municipio', ALPHABET + SPACE, 255)
        self.__entry_uf          = LabelEntry(
                self.__frame3_sub, 'UF', ALPHABET + SPACE, 255)
        self.__entry_cep         = LabelEntry(
                self.__frame3_sub, 'CEP', NUMERIC, 8)
        self.__entry_telefone   = LabelEntry(
                self.__frame4, 'Telefone', NUMERIC, 10)
        self.__entry_ncel        = LabelEntry(
                self.__frame4_sub, 'Celular', NUMERIC, 11)
        self.__entry_email       = LabelEntry(
                self, 'E-mail', ALPHANUMERIC + "_@-.", 255)
        self.__entry_url         = LabelEntry(
                self, 'URL', ALPHANUMERIC + "_-./", 255)

        self.__check_whatsapp = Checkbox(self.__frame4_sub, 'WhatsApp?')

        self.__button_cancelar  = Button(self, text="Cancelar",
                command=self.destroy)
        self.__button_salvar    = Button(self, text="Salvar")
        
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

        self.__frame0.add(self.__entry_nfantasia)
        self.__frame0.add(self.__entry_cnpj)
        self.__frame1.add(self.__entry_iestadual)
        self.__frame1.add(self.__entry_imunicipal)
        self.__frame2.add(self.__entry_complemento)
        self.__frame2.add(self.__entry_bairro)

        self.__frame3_sub.add(self.__entry_uf)
        self.__frame3_sub.add(self.__entry_cep)
        self.__frame3.add(self.__entry_municipio)
        self.__frame3.add(self.__frame3_sub)

        self.__frame4_sub.add(self.__entry_ncel)
        self.__frame4_sub.add(self.__check_whatsapp, 0, 'g2')
        self.__frame4.add(self.__entry_telefone)
        self.__frame4.add(self.__frame4_sub)

        self.__entry_rsocial.pack(fill='x', pady=3)
        self.__entry_rsocial.focus()

        self.__frame0.pack(fill='x', pady=3)
        self.__frame1.pack(fill='x', pady=3)

        self.__entry_logradouro.pack(fill='x', pady=3)

        self.__frame2.pack(fill='x', pady=3)
        self.__frame3.pack(fill='x', pady=3)
        self.__frame4.pack(fill='x', pady=3)

        self.__entry_email.pack(fill='x', pady=3)
        self.__entry_url.pack(fill='x', pady=3)

        self.__button_cancelar.pack(pady=3, padx=3, side=RIGHT)
        self.__button_salvar.pack(pady=3, side=RIGHT)

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
