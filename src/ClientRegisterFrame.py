from tkinter import *
from LabelEntry import *
from ColumnSplitter import *
from LabelEntryCheckbox import *
from TwoLabelEntry import *

class ClientRegisterFrame(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.__socialReason = LabelEntry(self, textLabel='Razão Social')
        self.__socialReason.pack(fill='x', pady=3)

        self.__tle0 = TwoLabelEntry(container=self, textLabel0='Nome Fantasia', textLabel1='CNPJ')
        self.__tle0.pack(fill='x', pady=3)

        self.__tle1 = TwoLabelEntry(container=self, textLabel0='Inscrição Estadual', textLabel1='Inscrição Municipal')
        self.__tle1.pack(fill='x', pady=3)

        self.__publicPlace = LabelEntry(container=self, textLabel='Logradouro')
        self.__publicPlace.pack(fill='x', pady=3)
        
        self.__tle2 = TwoLabelEntry(container=self, textLabel0='Complemento', textLabel1='Bairro')
        self.__tle2.pack(fill='x', pady=3)

        self.__cs0 = ColumnSplitter(container=self)
        self.__county = self.__cs0.addWidget(widget=LabelEntry(self.__cs0, textLabel='Município'))
        self.__cs0.addWidget(widget=TwoLabelEntry(container=self.__cs0, textLabel0='UF', textLabel1='CEP'))
        self.__cs0.pack(fill='x', pady=3)

        self.__cs1 = ColumnSplitter(container=self)
        self.__telephones = self.__cs1.addWidget(widget=LabelEntry(container=self.__cs1, textLabel='Telefones'))
        self.__cs1.addWidget(widget=LabelEntryCheckbox(container=self.__cs1, textLabel='Celular', textCheckbox='WhatsApp?'))
        self.__cs1.pack(fill='x', pady=3)

        self.__email = LabelEntry(container=self, textLabel="E-mail")
        self.__email.pack(fill='x', pady=3)

        self.__url = LabelEntry(container=self, textLabel="URL")
        self.__url.pack(fill='x', pady=3)

    def getSocialReason(self):
        return self.__socialReason.getValue()

    def getFantasyName(self):
        return self.__tle0.getLabelEntry0Value()

    def getCNPJ(self):
        return self.__tle0.getLabelEntry1Value()

    def getStateRegistration(self):
        return self.__tle1.getLabelEntry0Value()

    def getMunicipalRegistration(self):
        return self.__tle1.getLabelEntry1Value()

    def getPublicPlace(self):
        return self.__publicPlace.getValue()

    def getComplement(self):
        return self.__tle2.getLabelEntry0Value()

    def getNeighborhood(self):
        return self.__tle2.getLabelEntry1Value()

    def getCounty(self):
        return self.__cs0.getWidget(0).getValue()

    def getUF(self):
        return self.__cs0.getWidget(1).getLabelEntry0Value()

    def getCEP(self):
        return self.__cs0.getWidget(1).getLabelEntry1Value()

    def getTelephones(self):
        return self.__cs1.getWidget(0).getValue()

    def getCellphone(self):
        return self.__cs1.getWidget(1).getLabelEntryValue()

    def isWhatsApp(self):
        return self.__cs1.getWidget(1).getCheckboxValue()

    def getEmail(self):
        return self.__email.getValue()

    def getURL(self):
        return self.__url.getValue()

