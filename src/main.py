#!/usr/bin/env python3

import mysql.connector

from tkinter import *

VOWEL = "aeiou" 
VOWELACCENT = "áäàãéëèẽíïìĩóöòõúüùũ"
CONSONANTS = "bcdfghjklmnpqrstwxyz"
ALPHABET = VOWEL + VOWEL.upper() + VOWELACCENT + VOWELACCENT.upper() + CONSONANTS + CONSONANTS.upper()
NUMERIC = "1234567890"
ALPHANUMERIC = ALPHABET + NUMERIC
SYMBOLS = "!@#$%^&*()_-+=\\/?.,<>'\"[]{}"
ALPHANUMERICSYMBOLIC = ALPHANUMERIC + SYMBOLS
SPACE = " "

class LabelEntry(Frame):
    def __init__(self, master, text, mask, lenght):
        super().__init__(master)
        self.__label = Label(master=self, text=text, anchor='w')
        self.__label.grid(row=0, column=0, stick='w')
        self.__var = StringVar()
        self.__mask = mask
        self.__lenght = lenght
        self.__entry = Entry(self, textvariable=self.__var)
        self.__var.trace("w", lambda name, index, mode, var=self.__var:self.__update())
        self.__entry.grid(row=1, column=0, stick='nsew')
        self.__rule_list = []
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

    def rule_add(self, pos, symbol):
        self.__rule_list.append([pos+len(self.__rule_list), symbol])
        self.__lenght += len(symbol)
        return self

    def get_raw(self):
        text = self.get()
        len_text = len(text)
        tmp_rule_list = [e for e in self.__rule_list]
        while len(tmp_rule_list) != 0:
            tmp_pos = tmp_rule_list[0][0]
            if len_text > tmp_pos:
                text = text[:tmp_pos] + text[tmp_pos+1:]
                del tmp_rule_list[0]
                for i in range(0, len(tmp_rule_list)):
                    if tmp_rule_list[i][0] > tmp_pos:
                        tmp_rule_list[i][0] -= 1
            else:
                del tmp_rule_list[0]
        return text

    def set_raw(self, value):
        len_value = len(value)
        for i in self.__rule_list:
            if len_value > i[0]:
                value = value[:i[0]] + i[1] + value[i[0]:]
                len_value += 1 
        self.set(value)
                
    def get(self):
        return self.__entry.get()

    def set(self, value):
        self.__entry.delete(0, END)
        self.__entry.insert(0, value)

    def insert(self, value):
        text = self.get()
        self.__entry.insert(END, value)
        self.__entry.icursor(len(text)+1)

    def focus(self):
        self.__entry.focus()

    def __update(self):
        text = self.get()
        len_text = len(text)
        len_rule = len(self.__rule_list)

        if len_text > 0:
            if len_text < self.__lenght:
                if (len_rule > 0):
                    for rule in self.__rule_list:
                        if len_text == (rule[0]+1):
                            final_text = text[:-1] + rule[1] + text[-1]
                            self.set(final_text)
                        elif text[-1] == rule[1] or not text[-1] in self.__mask:
                            self.set(text[:-1])
                else:
                    if not text[-1] in self.__mask:
                        self.set(text[:-1])
            else:
                self.set(text[:self.__lenght])

            if len_rule > 0:
                if text[-1] == self.__rule_list[-1][1]:
                    self.set(text[:-1])

class DivisorColunas(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__widgets = []
        self.grid_rowconfigure(index=0, weight=1)

    def add(self, widget, weight=1, uniform='g1'):
        self.__widgets.append(widget)
        tamanho_lista = len(self.__widgets) - 1
        self.grid_columnconfigure(index=tamanho_lista, weight=weight, uniform=uniform)
        self.__widgets[tamanho_lista].grid(row=0, column=tamanho_lista, stick='nsew')

class Deposito(object):
    def __init__(self, user, passwd, host, db):
        self.__conn = mysql.connector.connect(
                user=user, password=passwd, host=host, database=db
        )
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

    def select(self, table, fields, where_fields = None, where_values = None, order_by = None, limit = None, offset = None):
        db_query = "SELECT " + self.__concat(fields) + " FROM " + table
        if (where_fields != None or where_values != None):
            db_query += " WHERE " + self.__concat_values(where_fields, where_values) 
            where = True
        if (order_by != None):
            db_query += " ORDER BY " + order_by
        if (limit != None):
            db_query += " LIMIT " + limit
        if (offset != None):
            db_query += " OFFSET " + offset
        return self.__query_fetchall(db_query)

    def insert(self, table, fields, values):
        db_query = "INSERT INTO " + table + " (" + self.__concat(fields) + ") VALUES ("
        db_query += self.__concat_format(values) + ")" 
        self.__query_commit(db_query)

    def delete(self, table, where_fields, where_values):
        db_query = "DELETE FROM " + table + " WHERE "
        db_query += self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

    def update(self, table, set_fields, set_values, where_fields, where_values):
        db_query = "UPDATE " + table + " SET " + self.__concat_values(set_fields, set_values) 
        db_query += " WHERE " + self.__concat_values(where_fields, where_values)
        self.__query_commit(db_query)

class JanelaCentralizada(Tk):
    def __init__(self, largura, altura, titulo):
        super().__init__()
        self.geometry("{}x{}+{}+{}".format(
            largura, altura,
            self.winfo_screenwidth()//2 - largura//2,
            self.winfo_screenheight()//2 - altura//2
            )
        )
        self.title(titulo)
        self.resizable(False, False)

class RegistroCliente(JanelaCentralizada):
    def __init__(self):
        super().__init__(800, 487, 'Cadastro Cliente')

        self.__frame = Frame(self)

        self.__frame0 = DivisorColunas(self.__frame)
        self.__frame1 = DivisorColunas(self.__frame)
        self.__frame2 = DivisorColunas(self.__frame)
        self.__frame3 = DivisorColunas(self.__frame)
        self.__frame4 = DivisorColunas(self.__frame)

        self.__frame3_sub = DivisorColunas(self.__frame3)
        self.__frame4_sub = DivisorColunas(self.__frame4)
        
        self.__frame_whatsapp = Frame(self.__frame4_sub)
        
        self.__label_whatsapp    = Label(self.__frame_whatsapp, text='')

        self.__entry_rsocial     = LabelEntry(
                self.__frame, 'Razão Social', ALPHANUMERIC + SPACE, 255)
        self.__entry_nfantasia   = LabelEntry(
                self.__frame0, 'Nome Fantasia', ALPHANUMERIC + SPACE, 255)
        self.__entry_cnpj        = LabelEntry(
                self.__frame0, 'CNPJ', NUMERIC, 14)
        self.__entry_iestadual   = LabelEntry(
                self.__frame1, 'Inscrição Estadual', NUMERIC, 12)
        self.__entry_imunicipal  = LabelEntry(
                self.__frame1, 'Inscrição Municipal', NUMERIC, 8)
        self.__entry_logradouro  = LabelEntry(
                self.__frame, 'Logradouro', ALPHANUMERIC + SPACE, 255)
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
        self.__entry_telefones   = LabelEntry(
                self.__frame4, 'Telefone', NUMERIC, 10)
        self.__entry_ncel        = LabelEntry(
                self.__frame4_sub, 'Celular', NUMERIC, 11)
        self.__entry_email       = LabelEntry(
                self.__frame, 'E-mail', ALPHANUMERIC + "_@-.", 255)
        self.__entry_url         = LabelEntry(
                self.__frame, 'URL', ALPHANUMERIC + "_-./", 255)

        self.__whatsapp = IntVar()
        self.__check_whatsapp = Checkbutton(self.__frame_whatsapp,
                text='WhatsApp?', variable=self.__whatsapp, width=9)

        self.__button_cancelar  = Button(self.__frame, text="Cancelar",
                command=self.destroy)
        self.__button_salvar    = Button(self.__frame, text="Salvar")
        
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
        
        self.__entry_telefones.rule_add(0, '(')
        self.__entry_telefones.rule_add(2, ') ')
        self.__entry_telefones.rule_add(7, '-')
        
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

        self.__label_whatsapp.pack()
        self.__check_whatsapp.pack()
        self.__frame4_sub.add(self.__entry_ncel)
        self.__frame4_sub.add(self.__frame_whatsapp, 0, 'g2')
        self.__frame4.add(self.__entry_telefones)
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
        self.__frame.pack(fill='both', padx=10, pady=10)

def main():
    instancia_registro = RegistroCliente()
    instancia_registro.mainloop()

if __name__ == "__main__":
    main()
