from tkinter import *
import tkinter.ttk as ttk
import os

from Tracer import *

class ClientForm(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        if os.name == "nt":
            self.geometry("{}x{}+{}+{}".format(
                800, 467,
                self.winfo_screenwidth()//2 - 800//2,
                self.winfo_screenheight()//2 - 487//2
                )
            )
        else:
            self.geometry("{}x{}+{}+{}".format(
                800, 487,
                self.winfo_screenwidth()//2 - 800//2,
                self.winfo_screenheight()//2 - 487//2
                )
            )
        self.resizable(False, False)

        self.__frame_border = Frame(self)
        
        self.__label_rsocial = Label(self.__frame_border,
                text='Razão Social')
        self.__label_nfantasia = Label(self.__frame_border,
                text='Nome Fantasia')
        self.__label_cnpj = Label(self.__frame_border,
                text='CNPJ')
        self.__label_iestadual = Label(self.__frame_border,
                text='Inscrição Estadual')
        self.__label_imunicipal = Label(self.__frame_border,
                text='Inscrição Municipal')
        self.__label_logradouro = Label(self.__frame_border,
                text='Logradouro')
        self.__label_complemento = Label(self.__frame_border,
                text='Complemento')
        self.__label_bairro = Label(self.__frame_border,
                text='Bairro')
        self.__label_municipio = Label(self.__frame_border,
                text='Municipio')
        self.__label_uf = Label(self.__frame_border,
                text='UF')
        self.__label_cep = Label(self.__frame_border,
                text='CEP')
        self.__label_telefone = Label(self.__frame_border,
                text='Telefone')
        self.__label_ncel = Label(self.__frame_border,
                text='Celular')
        self.__label_email = Label(self.__frame_border,
                text='E-mail')
        self.__label_url = Label(self.__frame_border,
                text='URL')
        
        self.__str_rsocial = StringVar()
        self.__str_nfantasia = StringVar()
        self.__str_cnpj = StringVar()
        self.__str_iestadual = StringVar()
        self.__str_imunicipal = StringVar()
        self.__str_logradouro = StringVar()
        self.__str_complemento = StringVar()
        self.__str_bairro = StringVar()
        self.__str_municipio = StringVar()
        self.__str_uf = StringVar()
        self.__str_cep = StringVar()
        self.__str_telefone = StringVar()
        self.__str_ncel = StringVar()

        self.__int_whatsapp = IntVar()

        self.__str_email = StringVar()
        self.__str_url = StringVar()
        
        self.__entry_rsocial = Entry(self.__frame_border,
                textvariable=self.__str_rsocial)
        self.__entry_nfantasia = Entry(self.__frame_border,
                textvariable=self.__str_nfantasia)
        self.__entry_cnpj = Entry(self.__frame_border,
                textvariable=self.__str_cnpj)
        self.__entry_iestadual = Entry(self.__frame_border,
                textvariable=self.__str_iestadual)
        self.__entry_imunicipal = Entry(self.__frame_border,
                textvariable=self.__str_imunicipal)
        self.__entry_logradouro = Entry(self.__frame_border,
                textvariable=self.__str_logradouro)
        self.__entry_complemento = Entry(self.__frame_border,
                textvariable=self.__str_complemento)
        self.__entry_bairro = Entry(self.__frame_border,
                textvariable=self.__str_bairro)

        self.__combo_municipio = ttk.Combobox(self.__frame_border,
                textvariable=self.__str_municipio)
        
        self.__combo_uf = ttk.Combobox(self.__frame_border,
                state="readonly", textvariable=self.__str_uf)

        self.__entry_cep = Entry(self.__frame_border,
                textvariable=self.__str_cep)
        self.__entry_telefone = Entry(self.__frame_border,
                textvariable=self.__str_telefone)
        self.__entry_ncel = Entry(self.__frame_border,
                textvariable=self.__str_ncel)
        
        self.__check_whatsapp = Checkbutton(self.__frame_border,
                text='WhatsApp?', variable=self.__int_whatsapp, width=9)

        self.__entry_email = Entry(self.__frame_border,
                textvariable=self.__str_email)
        self.__entry_url = Entry(self.__frame_border,
                textvariable=self.__str_url)
        
        self.__button_salvar = Button(
                self.__frame_border, text="Salvar")
        self.__button_cancelar = Button(
                self.__frame_border, text="Cancelar")

        self.__rule_rsocial = [ 
                ALPHANUMERIC + SPACE, 255 ]
        self.__rule_nfantasia = [ 
                ALPHANUMERIC + SPACE, 255 ]
        self.__rule_cnpj = [ 
                NUMERIC, 14, [2, '.'], [5, '.'], [8, '/'], [12, '-'] ]
        self.__rule_iestadual = [ 
                NUMERIC, 12, [3, '.'], [6, '.'], [9, '.'] ]
        self.__rule_imunicipal = [
                NUMERIC, 8, [1, '.'], [4, '.'], [7, '-'] ]
        self.__rule_logradouro = [ 
                ALPHANUMERIC + SPACE, 255 ]
        self.__rule_complemento = [ 
                ALPHANUMERIC + SPACE, 255 ]
        self.__rule_bairro = [ 
                ALPHABET + SPACE, 255 ]
        self.__rule_municipio = [ 
                ALPHABET + SPACE, 255 ]
        self.__rule_uf = [ 
                ALPHABET + SPACE, 255 ]
        self.__rule_cep = [ 
                NUMERIC, 8, [5, '-'] ]
        self.__rule_telefone = [
                NUMERIC, 30,
                [0, '('],
                [2, ') '],
                [7, '-'],
                [11, '; ('],
                [15, ') '],
                [20, '-'],
                [24, '; ('],
                [28, ') '],
                [33, '-']
                ]
        self.__rule_ncel = [ 
                NUMERIC, 11, [0, '('], [2, ') '], [4, ' '], [8, '-'] ]
        self.__rule_email = [ 
                ALPHANUMERIC + "_@-.", 255 ]
        self.__rule_url = [ 
                ALPHANUMERIC + "_-./:", 255 ]

        self.__tracer_rsocial = Tracer(self.__entry_rsocial,
                self.__rule_rsocial)
        self.__tracer_nfantasia = Tracer(self.__entry_nfantasia,
                self.__rule_nfantasia)
        self.__tracer_cnpj = Tracer(self.__entry_cnpj,
                self.__rule_cnpj, zeroes=True)
        self.__tracer_iestadual = Tracer(self.__entry_iestadual,
                self.__rule_iestadual, zeroes=True)
        self.__tracer_imunicipal = Tracer(self.__entry_imunicipal,
                self.__rule_imunicipal, zeroes=True)
        self.__tracer_logradouro = Tracer(self.__entry_logradouro,
                self.__rule_logradouro)
        self.__tracer_complemento = Tracer(self.__entry_complemento,
                self.__rule_complemento)
        self.__tracer_bairro = Tracer(self.__entry_bairro,
                self.__rule_bairro)
        self.__tracer_municipio = Tracer(self.__combo_municipio,
                self.__rule_municipio)
        self.__tracer_cep = Tracer(self.__entry_cep,
                self.__rule_cep, zeroes=True)
        self.__tracer_telefone = Tracer(self.__entry_telefone,
                self.__rule_telefone)
        self.__tracer_ncel = Tracer(self.__entry_ncel,
                self.__rule_ncel)
        self.__tracer_email = Tracer(self.__entry_email,
                self.__rule_email)
        self.__tracer_url = Tracer(self.__entry_url,
                self.__rule_url)
        
        self.__str_rsocial.trace("w", self.__tracer_rsocial.update)
        self.__str_nfantasia.trace("w", self.__tracer_nfantasia.update)
        self.__str_cnpj.trace("w", self.__tracer_cnpj.update)
        self.__str_iestadual.trace("w", self.__tracer_iestadual.update)
        self.__str_imunicipal.trace("w", self.__tracer_imunicipal.update)
        self.__str_logradouro.trace("w", self.__tracer_logradouro.update)
        self.__str_complemento.trace("w", self.__tracer_complemento.update)
        self.__str_bairro.trace("w", self.__tracer_bairro.update)
        self.__str_municipio.trace("w", self.__tracer_municipio.update)
        self.__str_cep.trace("w", self.__tracer_cep.update)
        self.__str_telefone.trace("w", self.__tracer_telefone.update)
        self.__str_ncel.trace("w", self.__tracer_ncel.update)
        self.__str_email.trace("w", self.__tracer_email.update)
        self.__str_url.trace("w", self.__tracer_url.update)
        
        self.__frame_border.grid_columnconfigure(index=0, minsize=1, weight=5)
        self.__frame_border.grid_columnconfigure(index=1, minsize=1, weight=1)
        self.__frame_border.grid_columnconfigure(index=2, minsize=1, weight=1)
       
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

        self.__entry_rsocial.grid(row=1, column=0, columnspan=6,
                stick='ew', pady=3)
        self.__entry_nfantasia.grid(row=3, column=0,
                stick='ew', pady=3)
        self.__entry_cnpj.grid(row=3, column=1, columnspan=5,
                stick='ew', pady=3)
        self.__entry_iestadual.grid(row=5, column=0,
                stick='ew', pady=3)
        self.__entry_imunicipal.grid(row=5, column=1, columnspan=5,
                stick='ew', pady=3)
        self.__entry_logradouro.grid(row=7, column=0, columnspan=6,
                stick='ew', pady=3)
        self.__entry_complemento.grid(row=9, column=0,
                stick='ew', pady=3)
        self.__entry_bairro.grid(row=9, column=1, columnspan=5,
                stick='ew', pady=3)
        self.__combo_municipio.grid(row=11, column=0,
                stick='ew', pady=3)
        self.__combo_uf.grid(row=11, column=1, columnspan=2,
                stick='ew', pady=3)
        self.__entry_cep.grid(row=11, column=3, columnspan=4,
                stick='ew', pady=3)
        self.__entry_telefone.grid(row=13, column=0,
                stick='ew', pady=3)
        self.__entry_ncel.grid(row=13, column=1, columnspan=4,
                stick='ew', pady=3)
        self.__check_whatsapp.grid(row=13, column=5,
                stick='nsew', pady=3)
        self.__entry_email.grid(row=15, column=0, columnspan=6,
                stick='ew', pady=3)
        self.__entry_url.grid(row=17, column=0, columnspan=6,
                stick='ew', pady=3)

        self.__button_salvar.grid(row=18, column=4, stick='e', pady=3)
        self.__button_cancelar.grid(row=18, column=5, stick='e', pady=3)

        self.grid_columnconfigure(index=0, minsize=1, weight=1)

        self.__frame_border.grid(row=0, column=0,
                stick='ew', padx=10, pady=10)

