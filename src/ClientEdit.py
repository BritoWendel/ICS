from tkinter import messagebox

from ClientInsert import *

class ClientEdit(ClientInsert):
    def __init__(self, db, id_cliente, master):
        super().__init__(db, master)
        self.title('Editar Cliente')

        self.__id_cliente = id_cliente
        self.__list = master
        
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
        
        self._ClientForm__button_salvar.config(
                command=self.__button_salvar_action)

        for i in range(0, len(self._ClientInsert__list_ufs)):
            if self._ClientInsert__list_ufs[i] == table_uf['nome_uf']:
                self._ClientForm__combo_uf.current(i)
        
        for i in range(0, len(self._ClientInsert__list_municipios)):
            if self._ClientInsert__list_municipios[i] == table_municipio['nome_municipio']:
                self._ClientForm__combo_municipio.current(i)
    
    def __button_salvar_action(self):
        data = self._ClientInsert__data_validation()
        if data == None:
            return
        else:
            self.__database_update(data)

    def __database_update(self, data):
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
        
        uf_id = str(self._ClientInsert__db.select("UF",
                ['id_uf'], ['nome_uf'], [uf])[0]['id_uf'])
        
        municipio_id = self._ClientInsert__db.select("MUNICIPIO",
                ['id_municipio'],
                ['nome_municipio', 'id_uf_municipio'],
                [municipio, uf_id])
        
        if len(municipio_id) == 0:
            self._ClientInsert__db.insert("MUNICIPIO", 
                    ['nome_municipio', 'id_uf_municipio'],
                    [municipio, uf_id])
            municipio_id = str(
                    self._ClientInsert__db.last_insert_id()[0]['LAST_INSERT_ID()'])
        else:
            municipio_id = str(municipio_id[0]['id_municipio'])

        self._ClientInsert__db.update("CLIENTE", 
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
                 municipio_id],
                ['id_cliente'],
                [str(self.__id_cliente)])

        table_telefone_id = self._ClientInsert__db.select("TELEFONE",
                ['id_telefone'],
                ['id_cliente_telefone'],
                [str(self.__id_cliente)])

        self._ClientInsert__db.update("TELEFONE",
                ['ddd_telefone',
                 'numero_telefone'],
                [self._ClientInsert__ddd_telefone,
                 self._ClientInsert__number_telefone],
                ['id_telefone'],
                [str(table_telefone_id[0]['id_telefone'])])
        
        self._ClientInsert__db.update("TELEFONE",
                ['ddd_telefone',
                 'numero_telefone'],
                [self._ClientInsert__ddd_telefone2,
                 self._ClientInsert__number_telefone2],
                ['id_telefone'],
                [str(table_telefone_id[1]['id_telefone'])])
        
        self._ClientInsert__db.update("TELEFONE",
                ['ddd_telefone',
                 'numero_telefone'],
                [self._ClientInsert__ddd_telefone3,
                 self._ClientInsert__number_telefone3],
                ['id_telefone'],
                [str(table_telefone_id[2]['id_telefone'])])
        
        messagebox.showinfo("Informação", "Dados alterados!", parent=self)

        self.destroy()
        self.__list.filter_client()

