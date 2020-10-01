from tkinter import *
from LabelEntry import *
from ColumnSplitter import *
from LabelEntryCheckbox import *
from TwoLabelEntry import *

class ClientRegisterFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.__socialReason = LabelEntry(self, text='Razão Social', mask="abcdefghijklmnopqrstuwxyz", max_lenght=5)
        self.__socialReason.pack(fill='x', pady=3)

#        self.__tle = TwoLabelEntry(master=self, text='Nome Fantasia', text1='CNPJ')
#        self.__tle.pack(fill='x', pady=3)
#
#        self.__tle1 = TwoLabelEntry(master=self, text='Inscrição Estadual', text1='Inscrição Municipal')
#        self.__tle1.pack(fill='x', pady=3)
#
#        self.__publicPlace = LabelEntry(master=self, text='Logradouro')
#        self.__publicPlace.pack(fill='x', pady=3)
#        
#        self.__tle2 = TwoLabelEntry(master=self, text='Complemento', text1='Bairro')
#        self.__tle2.pack(fill='x', pady=3)
#
#        self.__cs = ColumnSplitter(master=self)
#        self.__county = self.__cs.add(widget=LabelEntry(self.__cs, text='Município'))
#        self.__cs.add(widget=TwoLabelEntry(master=self.__cs, text='UF', text1='CEP'))
#        self.__cs.pack(fill='x', pady=3)
#
#        self.__cs1 = ColumnSplitter(master=self)
#        self.__telephones = self.__cs1.add(widget=LabelEntry(master=self.__cs1, text='Telefones'))
#        self.__cs1.add(widget=LabelEntryCheckbox(master=self.__cs1, text='Celular', text1='WhatsApp?'))
#        self.__cs1.pack(fill='x', pady=3)
#
#        self.__email = LabelEntry(master=self, text="E-mail")
#        self.__email.pack(fill='x', pady=3)
#
#        self.__url = LabelEntry(master=self, text="URL")
#        self.__url.pack(fill='x', pady=3)
#
#        self.__saveButton = Button(master=self, text="Cancelar")
#        self.__saveButton.pack(pady=3, padx=3, side=RIGHT)
#
#        self.__cancelButton = Button(master=self, text="Salvar")
#        self.__cancelButton.pack(pady=3, side=RIGHT)

    def getSocialReason(self):
        return self.__socialReason.get()

    def getFantasyName(self):
        return self.__tle.get(0)

    def getCNPJ(self):
        return self.__tle.get(1)

    def getStateRegistration(self):
        return self.__tle1.get(0)

    def getMunicipalRegistration(self):
        return self.__tle1.get(1)

    def getPublicPlace(self):
        return self.__publicPlace.get()

    def getComplement(self):
        return self.__tle2.get(0)

    def getNeighborhood(self):
        return self.__tle2.get(1)

    def getCounty(self):
        return self.__cs.get(0).get()

    def getUF(self):
        return self.__cs.get(1).get(0)

    def getCEP(self):
        return self.__cs.get(1).get(1)

    def getTelephones(self):
        return self.__cs1.get(0).get()

    def getCellphone(self):
        return self.__cs1.get(1).get(0)

    def isWhatsApp(self):
        return self.__cs1.get(1).get(1)

    def getEmail(self):
        return self.__email.get()

    def getURL(self):
        return self.__url.get()

