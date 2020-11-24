#!/usr/bin/env python3
#
# ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# Programação Avançada
# 4ADS | 2020-2
#
# Integrated Corporate System
#
# Equipe 02
#   Wendel Rodrigues Ferreira Brito, 25306 (Lider)
#   Aline Aparecida Vicente de Souza, 25604
#   André Ricardo Capeleto, 25396
#   Jeferson Luiz Butinhão de Oliveira, 25473
#   João Gabriel Sabatini, 25471
#   Rodney de Andrade Martins, 25305
#   Tiffany Carvalho das Neves, 25591
#

import os
import sys
import time
import math
import re

import mysql.connector
from mysql.connector import errorcode

from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

VOWEL_LOWER = "aeiou"
VOWEL_UPPER = VOWEL_LOWER.upper()
VOWEL = VOWEL_LOWER + VOWEL_UPPER
VOWEL_ACCENT_LOWER = "áäàãéëèẽíïìĩóöòõúüùũ"
VOWEL_ACCENT_UPPER = VOWEL_ACCENT_LOWER.upper()
VOWEL_ACCENT = VOWEL_ACCENT_LOWER + VOWEL_ACCENT_UPPER
VOWEL_FULL = VOWEL + VOWEL_ACCENT
CONSONANTS_LOWER = "bcçdfghjklmnpqrstvwxyz"
CONSONANTS_UPPER = CONSONANTS_LOWER.upper()
CONSONANTS = CONSONANTS_LOWER + CONSONANTS_UPPER
ALPHABET = VOWEL_FULL + CONSONANTS 
NUMERIC = "1234567890"
ALPHANUMERIC = ALPHABET + NUMERIC
SYMBOLS = "!@#$%^&*()_-+=\\/?.,<>'\"[]{}"
SPACE = " "

class Tracer(object):
    def __init__(self, entry, rules, zeroes=None):
        self.__rules = rules
        self.__entry = entry
        self.__zeroes = zeroes
        
        for i in range(2, len(self.__rules)):
            self.__rules[i][0] += i - 2
            self.__rules[1] += len(self.__rules[i][1])
    
    def __replace(self, value):
        self.__entry.delete(0, 'end')
        self.__entry.insert(0, value)

    def get(self, entry_value=None):
        text = ""
        if entry_value == None:
            entry_value = self.__entry.get()

        if entry_value == "":
            return entry_value

        for char in entry_value:
            if char in self.__rules[0]:
                text += char
        return text

    def set(self, value):
        if value == '' or value == None:
            return
        len_value = len(value)
        real_size = self.__rules[1] - len(self.__rules[2:])
        zero_increment = ""
        if (len_value < real_size and
            self.__rules[0] == NUMERIC and
            self.__zeroes != None):
            for i in range(real_size-len_value):
                zero_increment += "0"
            value = zero_increment + value
            len_value = len(value)
        for i in range(2, len(self.__rules)):
            rule = self.__rules[i]
            if len_value > rule[0]:
                value = value[:rule[0]] + rule[1] + value[rule[0]:]
                len_value += len(rule[1])
        self.__replace(value)

    def update(self, *args):
        text = self.__entry.get()
        len_text = len(text)

        if len_text == 0:
            return

        if text[-1] not in self.__rules[0] or len_text > self.__rules[1]:
            if len_text > 1 and (text[-2] == ')' or text[-2] == ' '):
                if text[-3] == ';':
                    index = -3
                else:
                    index = -2
            else:
                index = -1
            self.__replace(text[:index])
            return

        for rule in self.__rules[2:]:
            if len_text == (rule[0]+1):
                self.__replace(text[:-1] + rule[1] + text[-1])
                return

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

class Database(object):
    def __create_connection(self):
        user = self.__user_entry.get()
        passwd = self.__pass_entry.get()
        try:
            self.__conn = mysql.connector.connect(
                    user=user, password=passwd, host='localhost',
                    database='sci_db', auth_plugin='mysql_native_password'
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.__user_label['fg'] = 'red'
                self.__pass_label['fg'] = 'red'
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                if (messagebox.showinfo("Informação",
                    "Erro o Schema `sci_db` não existe!")):
                    self.__dbwin.destroy()
            else:
                if (messagebox.showinfo("Informação", err)):
                    self.__dbwin.destroy()
        else:
            self.conn_error = False
            self.__dbwin.destroy()
            return

    def __init__(self):
        self.conn_error = True
        self.__dbwin = Tk()
        self.__dbwin.geometry("{}x{}+{}+{}".format(
            170, 115,
            self.__dbwin.winfo_screenwidth()//2 - 170//2,
            self.__dbwin.winfo_screenheight()//2 - 115//2
            )
        )
        self.__dbwin.resizable(False, False)
        self.__dbwin.title("Database Login")
        self.__user_label = Label(self.__dbwin, text="User:")
        self.__pass_label = Label(self.__dbwin, text="Pass:")
        self.__user_entry = Entry(self.__dbwin)
        self.__pass_entry = Entry(self.__dbwin, show="*")
        login_button = Button(self.__dbwin, text="Login",
                command=self.__create_connection)
        self.__dbwin.grid_columnconfigure(index=0, weight=1)
        self.__user_label.grid(row=0, column=0, sticky='w')
        self.__user_entry.grid(row=1, column=0, sticky='we')
        self.__pass_label.grid(row=2, column=0, sticky='w')
        self.__pass_entry.grid(row=3, column=0, sticky='we')
        login_button.grid(row=4, column=0, sticky='e')
        self.__dbwin.mainloop()

        if self.conn_error:
            return

        version_table = self.__query_fetchall(
                "SHOW VARIABLES LIKE \"%version%\"")
        self.version_error = True
        for entry in version_table:
            if (entry['Variable_name'] == 'version' and
            int(entry['Value'][0]) > 7):
                self.version_error = False
                return

    def __concat(self, fields):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i]
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_format(self, fields):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += "'" + fields[i] + "'"
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_values(self, fields, values):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i] + " = '" + values[i] + "'"
            if (i != tmp_len-1):
                tmp_str += ", "
        return tmp_str

    def __concat_values_and(self, fields, values):
        text = self.__concat_values(fields, values)
        for i in range(len(text)):
            if text[i] == ",":
                text = text[:i] + " AND" + text[i+1:]
        return text
    
    def __concat_like(self, fields, values):
        tmp_str = ""
        tmp_len = len(fields)
        for i in range(0, tmp_len):
            tmp_str += fields[i] + " LIKE \"%" + values[i] + "%\""
            if (i != tmp_len-1):
                tmp_str += " OR "
        return tmp_str

    def __query_exec(self, query):
        db_dict = self.__conn.cursor(dictionary=True)
        db_dict.execute(query)
        return db_dict

    def __query_commit(self, query):
        db_dict = self.__query_exec(query)
        self.__conn.commit()
        db_dict.close()
    
    def __query_fetchall(self, query):
        db_dict = self.__query_exec(query)
        db_data = db_dict.fetchall()
        db_dict.close()
        return db_data
    
    def last_insert_id(self):
        return self.__query_fetchall("SELECT LAST_INSERT_ID()")

    def select(self, table, fields, where_fields = None, where_values = None,
            order_by = None, limit = None, offset = None, like = None):
        db_query = "SELECT " + self.__concat(fields) + " FROM " + table
        if (where_fields != None and where_values != None):
            db_query += " WHERE "
            if (like):
                db_query += self.__concat_like(where_fields, where_values) 
            else:
                db_query += self.__concat_values_and(where_fields, where_values) 
            where = True
        if (order_by != None):
            db_query += " ORDER BY " + order_by
        if (limit != None):
            db_query += " LIMIT " + limit
        if (offset != None):
            db_query += " OFFSET " + offset
        return self.__query_fetchall(db_query)

    def insert(self, table, fields, values):
        pointer = 0
        final_len = len(values)
        while pointer != final_len:
            if values[pointer] == '':
                del values[pointer]
                del fields[pointer]
            else:
                pointer += 1
            final_len = len(values)
        
        db_query = "INSERT INTO " + table + " (" 
        db_query += self.__concat(fields) + ") VALUES ("
        db_query += self.__concat_format(values) + ")" 
        self.__query_commit(db_query)

    def delete(self, table, where_fields, where_values):
        db_query = "DELETE FROM " + table + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

    def update(self, table, set_fields, set_values,
            where_fields, where_values):
        pointer = 0
        final_len = len(set_values)
        while pointer != final_len:
            if set_values[pointer] == '':
                del set_values[pointer]
                del set_fields[pointer]
            else:
                pointer += 1
            final_len = len(set_values)

        pointer = 0
        final_len = len(where_values)
        while pointer != final_len:
            if where_values[pointer] == '':
                del where_values[pointer]
                del where_fields[pointer]
            else:
                pointer += 1
            final_len = len(where_values)

        db_query = "UPDATE " + table + " SET " 
        db_query += self.__concat_values(set_fields, set_values) + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

    def close(self):
        self.__conn.close()

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

        if table_cliente['iestadual_cliente'] == None:
            self._ClientForm__tracer_iestadual.set('')
        else:
            self._ClientForm__tracer_iestadual.set(
                    str(table_cliente['iestadual_cliente']))

        if table_cliente['imunicipal_cliente'] == None:
            self._ClientForm__tracer_imunicipal.set('')
        else:
            self._ClientForm__tracer_imunicipal.set(
                    str(table_cliente['imunicipal_cliente']))

        self._ClientForm__str_logradouro.set(
                table_cliente['logradouro_cliente'])

        if table_cliente['complemento_cliente'] == None:
            self._ClientForm__str_complemento.set('')
        else:
            self._ClientForm__str_complemento.set(
                    table_cliente['complemento_cliente'])

        self._ClientForm__tracer_cep.set(
                str(table_cliente['cep_cliente']))
        self._ClientForm__tracer_telefone.set(
                telefones)

        if table_cliente['ddd_cel_cliente'] == None:
            celular = ""
        else:
            celular = str(table_cliente['ddd_cel_cliente'])

        if table_cliente['ncel_cliente'] == None:
            celular = ""
        else:
            celular += str(table_cliente['ncel_cliente'])
        
        self._ClientForm__str_bairro.set(
                table_cliente['bairro_cliente'])
        self._ClientForm__str_email.set(
                table_cliente['email_cliente'])

        if table_cliente['url_cliente'] == None:
            self._ClientForm__str_url.set('')
        else:
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

        if iestadual != "" and len(iestadual) < 12:
            self._ClientForm__label_iestadual.config(fg="red")
            error = True
        elif iestadual != "":
            w = [1, 3, 4, 5, 6, 7, 8, 10]
            w1 = [3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            verify = lambda a: str(z(a, iestadual))[-1] == iestadual[len(a)]
            if verify(w) and verify(w1):
                self._ClientForm__label_iestadual.config(fg="black")
            else:
                self._ClientForm__label_iestadual.config(fg="red")
                error = True

        imunicipal = self._ClientForm__tracer_imunicipal.get()

        if imunicipal != "" and len(imunicipal) < 8:
            self._ClientForm__label_imunicipal.config(fg="red")
            error = True
        elif imunicipal != "":
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

        self.__ddd_telefone2 = "00"
        self.__number_telefone2 = "00000000"
        self.__ddd_telefone3 = "00"
        self.__number_telefone3 = "00000000"
        
        self._ClientForm__label_telefone.config(fg="black")

        if (len_telefone == 10 and
            telefone[:2] in allowed_ddds and
            telefone[2:3] in first_digit):
            self.__ddd_telefone = telefone[:2]
            self.__number_telefone = telefone[2:10]
        elif (len_telefone == 20 and
              telefone[:2] in allowed_ddds and
              telefone[2:3] in first_digit and
              telefone[10:12] in allowed_ddds and
              telefone[12:13] in first_digit):
            self.__ddd_telefone = telefone[:2]
            self.__number_telefone = telefone[2:10]
            self.__ddd_telefone2 = telefone[10:12]
            self.__number_telefone2 = telefone[12:20]
        elif (len_telefone == 30 and
              telefone[:2] in allowed_ddds and
              telefone[2:3] in first_digit and
              telefone[10:12] in allowed_ddds and
              telefone[12:13] in first_digit and
              telefone[20:22] in allowed_ddds and
              telefone[22:23] in first_digit):
            self.__ddd_telefone = telefone[:2]
            self.__number_telefone = telefone[2:10]
            self.__ddd_telefone2 = telefone[10:12]
            self.__number_telefone2 = telefone[12:20]
            self.__ddd_telefone3 = telefone[20:22]
            self.__number_telefone3 = telefone[22:30]
        else:
            self._ClientForm__label_telefone.config(fg="red")
            error = True

        ncel = self._ClientForm__tracer_ncel.get()
        
        first_digit = ["6", "7", "8", "9"]

        if (ncel != "" and (len(ncel) < 11 or
            ncel[:2] not in allowed_ddds or
            ncel[3:4] not in first_digit)):
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

        if (url != "" and (pos < 3 or
            url[3:] in domain or
            url[3:] in domain_br or
            url[:4] != "www." or
            (url[len(url)-4:] not in domain and
             url[len(url)-7:] not in domain_br))):
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
            municipio_id = str(
                    self.__db.last_insert_id()[0]['LAST_INSERT_ID()'])
            print(municipio_id)
        else:
            municipio_id = str(municipio_id[0]['id_municipio'])

        try:
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
        except Exception as e:
            error_msg = str(e)
            x = re.search("'CLIENTE.*'$", error_msg)

            if not x:
                messagebox.showinfo("Informação",
                        "Erro desconhecido, contate o suporte!", parent=self)
            
            location = x.span()
            error_msg = error_msg[location[0]:location[1]]
            error_msg = re.sub("CLIENTE\.", "", error_msg)
            error_msg = error_msg[1:-1]

            if error_msg == "cnpj_cliente":
                self._ClientForm__label_cnpj.config(fg="red")
            elif error_msg == "iestadual_cliente":
                self._ClientForm__label_iestadual.config(fg="red")
            elif error_msg == "imunicipal_cliente":
                self._ClientForm__label_imunicipal.config(fg="red")
            elif error_msg == "rsocial_cliente":
                self._ClientForm__label_rsocial.config(fg="red")

    def __button_cancelar_action(self):
        if messagebox.askyesno("Alerta", "Realmente deseja sair?", parent=self):
            self.destroy()

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

        if table_cliente['iestadual_cliente'] == None:
            self._ClientForm__tracer_iestadual.set('')
        else:
            self._ClientForm__tracer_iestadual.set(
                    str(table_cliente['iestadual_cliente']))

        if table_cliente['imunicipal_cliente'] == None:
            self._ClientForm__tracer_imunicipal.set('')
        else:
            self._ClientForm__tracer_imunicipal.set(
                    str(table_cliente['imunicipal_cliente']))

        self._ClientForm__str_logradouro.set(
                table_cliente['logradouro_cliente'])
        
        if table_cliente['complemento_cliente'] == None:
            self._ClientForm__str_complemento.set('')
        else:
            self._ClientForm__str_complemento.set(
                    table_cliente['complemento_cliente'])

        self._ClientForm__tracer_cep.set(
                str(table_cliente['cep_cliente']))
        self._ClientForm__tracer_telefone.set(
                telefones)

        if table_cliente['ddd_cel_cliente'] == None:
            celular = ""
        else:
            celular = str(table_cliente['ddd_cel_cliente'])

        if table_cliente['ncel_cliente'] == None:
            celular = ""
        else:
            celular += str(table_cliente['ncel_cliente'])
        
        self._ClientForm__tracer_ncel.set(
                celular)
        
        self._ClientForm__str_bairro.set(
                table_cliente['bairro_cliente'])
        self._ClientForm__str_email.set(
                table_cliente['email_cliente'])

        if table_cliente['url_cliente'] == None:
            self._ClientForm__str_url.set('')
        else:
            self._ClientForm__str_url.set(table_cliente['url_cliente'])

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

        try:
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
        except Exception as e:
            error_msg = str(e)
            x = re.search("'CLIENTE.*'$", error_msg)

            if not x:
                messagebox.showinfo("Informação",
                        "Erro desconhecido, contate o suporte!", parent=self)
            
            location = x.span()
            error_msg = error_msg[location[0]:location[1]]
            error_msg = re.sub("CLIENTE\.", "", error_msg)
            error_msg = error_msg[1:-1]

            if error_msg == "cnpj_cliente":
                self._ClientForm__label_cnpj.config(fg="red")
            elif error_msg == "iestadual_cliente":
                self._ClientForm__label_iestadual.config(fg="red")
            elif error_msg == "imunicipal_cliente":
                self._ClientForm__label_imunicipal.config(fg="red")
            elif error_msg == "rsocial_cliente":
                self._ClientForm__label_rsocial.config(fg="red")

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
        if value == None:
            return ''
        if name == "cnpj_cliente":
            value = str(value)
            return value[:2] + "." + value[2:5] + "." + value[5:8] + "/" + value[8:12] + "." + value[12:15]
        if name == "iestadual_cliente":
            if str(value)[-4:] == "None":
                return ''
            value = str(value)
            return value[:3] + "." + value[3:6] + "." + value[6:9] + "." + value[9:]
        if name == "imunicipal_cliente":
            if str(value)[-4:] == "None":
                return ''
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
            field == "imunicipal_cliente" or field == "cep_cliente"):
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
                elif field == "cep_cliente":
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
        pag_number = math.ceil(len(self.__table_cliente[0])/20)
        tmp = []
        for i in range(pag_number):
            tmp.append(i)
        self.__combo_pagina['values'] = tmp
        try:
            self.__combo_pagina.current(0)
        except:
            pass

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
        return self.__table_cliente[0][selection+(20*int(self.__combo_pagina.get()))]

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
            selected_id = str(self.__get_client_id())
            self.__db.delete("TELEFONE",
                    ["id_cliente_telefone"], [selected_id])
            self.__db.delete("CLIENTE",
                    ["id_cliente"], [selected_id])
            self.filter_client()

def messagebox_info(msg):
    info_tk = Tk()
    info_tk.geometry("{}x{}+{}+{}".format(
        0, 0,
        info_tk.winfo_screenwidth()//2 - 0//2,
        info_tk.winfo_screenheight()//2 - 0//2
        )
    )
    info_tk.withdraw()
    if (messagebox.showinfo("Informação", msg)):
        info_tk.destroy()
        return

def main():
    if (sys.version_info.major < 3 or sys.version_info.minor < 7):
        messagebox_info(
                "Você não possui a versão mínima recomendada do Python")
        return
    
    if int(str(mysql.connector.__version__)[0]) < 8:
        messagebox_info(
                "Você não possui a versão mínima recomendada do MySQL Connector")
        return

    db = Database()
    
    if db.conn_error:
        return

    if db.version_error:
        messagebox_info(
                "Você não possui a versão mínima recomendada do MySQL Server")
        return

    instance_list = ClientList(db)
    instance_list.mainloop()
    db.close()

if __name__ == "__main__":
    main()

