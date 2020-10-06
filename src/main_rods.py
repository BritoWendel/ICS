import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import mysql.connector

###### DATABASE - INICIO ############################################

class Database:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.cnx = None

    def connect(self):
        self.cnx = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )

    def close(self):
        self.cnx.close()

    def get_pessoa_juridica(self, id):
        cursor = self.cnx.cursor(dictionary=True)
        cursor.execute("SELECT "
                       "id, "
                       "razao_social,"
                       "nome_fantasia,"
                       "cnpj,"
                       "inscricao_estadual,"
                       "inscricao_municipal,"
                       "endereco_logradouro,"
                       "endereco_complemento,"
                       "endereco_bairro,"
                       "endereco_municipio,"
                       "endereco_uf,"
                       "endereco_cep,"
                       "telefone_numero_1,"
                       "telefone_numero_2,"
                       "telefone_numero_3,"
                       "telefone_numero_4,"
                       "celular_numero_1,"
                       "celular_is_whatsapp_1,"
                       "email,"
                       "website FROM pessoa_juridica "
                       "WHERE id = %s", (id,))
        pj = cursor.fetchone()
        cursor.close()
        return pj

    def list_pessoa_juridica(self):
        cursor = self.cnx.cursor(dictionary=True)
        cursor.execute("SELECT id, razao_social, nome_fantasia, cnpj, inscricao_estadual, inscricao_municipal, endereco_logradouro, endereco_complemento, endereco_bairro, endereco_municipio, endereco_uf, endereco_cep, telefone_numero_1, telefone_numero_2, telefone_numero_3, telefone_numero_4, celular_numero_1, email, website FROM pessoa_juridica")
        list_pj = cursor.fetchall()
        cursor.close()
        return list_pj

    def insert_pessoa_juridica(self, pessoa_juridica):
        cursor = self.cnx.cursor()
        cursor.execute("INSERT INTO pessoa_juridica(razao_social, nome_fantasia, cnpj, inscricao_estadual, inscricao_municipal, endereco_logradouro, endereco_complemento, endereco_bairro, endereco_municipio, endereco_uf, endereco_cep, telefone_numero_1, telefone_numero_2, telefone_numero_3, telefone_numero_4, celular_numero_1, celular_is_whatsapp_1, email, website) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", pessoa_juridica)
        self.cnx.commit()
        cursor.close()

    def update_pessoa_juridica(self, pessoa_juridica):
        cursor = self.cnx.cursor()
        cursor.execute("UPDATE pessoa_juridica SET razao_social = %s, nome_fantasia = %s, cnpj = %s, inscricao_estadual = %s, inscricao_municipal = %s, endereco_logradouro = %s, endereco_complemento = %s, endereco_bairro = %s, endereco_municipio = %s, endereco_uf = %s, endereco_cep = %s, telefone_numero_1 = %s, telefone_numero_2 = %s, telefone_numero_3 = %s, telefone_numero_4 = %s, celular_numero_1 = %s, celular_is_whatsapp_1 = %s, email = %s, website = %s WHERE id = %s", pessoa_juridica)
        self.cnx.commit()
        cursor.close()

    def delete_pessoa_juridica(self, id):
        cursor = self.cnx.cursor()
        cursor.execute("DELETE FROM pessoa_juridica WHERE id = %s", (id,))
        self.cnx.commit()
        cursor.close()

###### DATABASE - FIM ############################################

###### FORMULARIO - LISTAGEM - INICIO ############################

class ListPessoaJuridica(tk.Frame):
    def __init__(self, db, form_pj, parent):
        super().__init__(parent)

        self.db = db
        self.form_pj = form_pj
        self.parent = parent

        self.selected_pessoa_juridica = None

        self.tree = ttk.Treeview(main)
        self.tree["columns"] = (1, 2, 3, 4, 5)
        self.tree["show"] = "headings"

        self.tree.heading(1, text="ID")
        self.tree.heading(2, text="Razão Social")
        self.tree.heading(3, text="Nome Fantasia")
        self.tree.heading(4, text="CNPJ")
        self.tree.heading(5, text="Inscrição Estadual")

        self.tree.column(1, width=50)
        self.tree.column(2, width=200)
        self.tree.column(3, width=200)
        self.tree.column(4, width=200)
        self.tree.column(5, width=200)

        self.tree.bind("<1>", self.tree_on_click)
        self.tree.pack(side=tk.BOTTOM)

        self.btn_create = ttk.Button(text="Novo", command=self.open_create_form)
        self.btn_create.pack(side=tk.LEFT)

        self.btn_update = ttk.Button(text="Alterar", command=self.open_update_form)
        self.btn_update.pack(side=tk.LEFT)

        self.btn_delete = ttk.Button(text="Excluir", command=self.open_delete_confirm)
        self.btn_delete.pack(side=tk.LEFT)

        self.load_tree()

    def tree_on_click(self, event):
        item = self.tree.identify("item", event.x, event.y)
        self.selected_pessoa_juridica = self.tree.item(item)['values'][0]

    def load_tree(self):
        self.tree.delete(*self.tree.get_children())
        for pj in self.db.list_pessoa_juridica():
            model = (
                pj["id"],
                pj["razao_social"],
                pj["nome_fantasia"],
                pj["cnpj"],
                pj["inscricao_estadual"]
            )
            self.tree.insert("", tk.END, values=model)

    def open_create_form(self):
        self.form_pj.open(self.parent, None)

    def open_update_form(self):
        if self.selected_pessoa_juridica is not None:
            self.form_pj.open(self.parent, self.selected_pessoa_juridica)

    def open_delete_confirm(self):
        if messagebox.askyesno("Confirmação", "Deseja realmente excluir este registro?"):
            self.db.delete_pessoa_juridica(self.selected_pessoa_juridica)
            self.load_tree()
            messagebox.showinfo("Alerta", "Registro excluído com sucesso")

###### FORMULARIO - LISTAGEM - FIM ############################

###### FORMULARIO - ALTERACAO - INICIO ########################

class FormPessoaJuridica(tk.Frame):
    def __init__(self, db, parent, confirm_callback):
        super().__init__(parent)
        self.db = db
        self.confirm_callback = confirm_callback
        self.window = tk.Toplevel(parent)
        self.window.withdraw()
        self.selected_pessoa_juridica = None

        ttk.Label(self.window, text="Razão Social").grid(row=0, column=0)
        self.entry_razao_social = ttk.Entry(self.window)
        self.entry_razao_social.grid(row=0, column=1)

        ttk.Label(self.window, text="Nome Fantasia").grid(row=1, column=0)
        self.entry_nome_fantasia = ttk.Entry(self.window)
        self.entry_nome_fantasia.grid(row=1, column=1)

        ttk.Label(self.window, text="CNPJ").grid(row=2, column=0)
        self.entry_cnpj = ttk.Entry(self.window)
        self.entry_cnpj.grid(row=2, column=1)

        ttk.Label(self.window, text="Inscrição Estadual").grid(row=3, column=0)
        self.entry_inscricao_estadual = ttk.Entry(self.window)
        self.entry_inscricao_estadual.grid(row=3, column=1)

        ttk.Label(self.window, text="Inscrição Municipal").grid(row=4, column=0)
        self.entry_inscricao_municipal = ttk.Entry(self.window)
        self.entry_inscricao_municipal.grid(row=4, column=1)

        ttk.Label(self.window, text="Logradouro").grid(row=5, column=0)
        self.entry_endereco_logradouro = ttk.Entry(self.window)
        self.entry_endereco_logradouro.grid(row=5, column=1)

        ttk.Label(self.window, text="Complemento").grid(row=6, column=0)
        self.entry_endereco_complemento = ttk.Entry(self.window)
        self.entry_endereco_complemento.grid(row=6, column=1)

        ttk.Label(self.window, text="Bairro").grid(row=7, column=0)
        self.entry_endereco_bairro = ttk.Entry(self.window)
        self.entry_endereco_bairro.grid(row=7, column=1)

        ttk.Label(self.window, text="Município").grid(row=8, column=0)
        self.entry_endereco_municipio = ttk.Entry(self.window)
        self.entry_endereco_municipio.grid(row=8, column=1)

        ttk.Label(self.window, text="UF").grid(row=9, column=0)
        self.entry_endereco_uf = ttk.Entry(self.window)
        self.entry_endereco_uf.grid(row=9, column=1)

        ttk.Label(self.window, text="CEP").grid(row=10, column=0)
        self.entry_endereco_cep = ttk.Entry(self.window)
        self.entry_endereco_cep.grid(row=10, column=1)
        #entry_endereco_cep.bind("<KeyRelease>", lambda e: mascara("cep", entry_endereco_cep))

        ttk.Label(self.window, text="Telefone 1").grid(row=11, column=0)
        self.entry_telefone_numero_1 = ttk.Entry(self.window)
        self.entry_telefone_numero_1.grid(row=11, column=1)

        ttk.Label(self.window, text="Telefone 2").grid(row=12, column=0)
        self.entry_telefone_numero_2 = ttk.Entry(self.window)
        self.entry_telefone_numero_2.grid(row=12, column=1)

        ttk.Label(self.window, text="Telefone 3").grid(row=13, column=0)
        self.entry_telefone_numero_3 = ttk.Entry(self.window)
        self.entry_telefone_numero_3.grid(row=13, column=1)

        ttk.Label(self.window, text="Telefone 4").grid(row=14, column=0)
        self.entry_telefone_numero_4 = ttk.Entry(self.window)
        self.entry_telefone_numero_4.grid(row=14, column=1)

        ttk.Label(self.window, text="Celular").grid(row=15, column=0)
        self.entry_celular_numero_1 = ttk.Entry(self.window)
        self.entry_celular_numero_1.grid(row=15, column=1)

        self.is_whatsapp = tk.IntVar()
        check_whatsapp = ttk.Checkbutton(self.window, text="Whatsapp", variable=self.is_whatsapp)
        check_whatsapp.grid(row=15, column=2)

        ttk.Label(self.window, text="E-mail").grid(row=16, column=0)
        self.entry_email = ttk.Entry(self.window)
        self.entry_email.grid(row=16, column=1)

        ttk.Label(self.window, text="Website").grid(row=17, column=0)
        self.entry_website = ttk.Entry(self.window)
        self.entry_website.grid(row=17, column=1)

        ttk.Button(self.window, text="Confirmar", command=self.confirm).grid(row=18, column=1)

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.window.withdraw()

    def open(self, parent, selected_pessoa_juridica):
        x = parent.winfo_rootx()
        y = parent.winfo_rooty()
        height = parent.winfo_height()
        hwidth = parent.winfo_width()
        self.window.geometry("+%d+%d" % (x + hwidth / 3, y + height / 3))
        self.window.deiconify()
        self.selected_pessoa_juridica = selected_pessoa_juridica

        if selected_pessoa_juridica is None:
            self.__clean_fields()
        else:
            pj = self.db.get_pessoa_juridica(self.selected_pessoa_juridica)
            self.__fill_pj(pj)

    def confirm(self):
        if self.selected_pessoa_juridica is None:
            pessoa_juridica = (
                self.entry_razao_social.get(),
                self.entry_nome_fantasia.get(),
                self.entry_cnpj.get(),
                self.entry_inscricao_estadual.get(),
                self.entry_inscricao_municipal.get(),
                self.entry_endereco_logradouro.get(),
                self.entry_endereco_complemento.get(),
                self.entry_endereco_bairro.get(),
                self.entry_endereco_municipio.get(),
                self.entry_endereco_uf.get(),
                self.entry_endereco_cep.get(),
                self.entry_telefone_numero_1.get(),
                self.entry_telefone_numero_2.get(),
                self.entry_telefone_numero_3.get(),
                self.entry_telefone_numero_4.get(),
                self.entry_celular_numero_1.get(),
                self.is_whatsapp.get(),
                self.entry_email.get(),
                self.entry_website.get()
            )
            self.db.insert_pessoa_juridica(pessoa_juridica)
            messagebox.showinfo("Alerta", "Cadastro efetuado com sucesso!")
        else:
            pessoa_juridica = (
                               self.entry_razao_social.get(),
                               self.entry_nome_fantasia.get(),
                               self.entry_cnpj.get(),
                               self.entry_inscricao_estadual.get(),
                               self.entry_inscricao_municipal.get(),
                               self.entry_endereco_logradouro.get(),
                               self.entry_endereco_complemento.get(),
                               self.entry_endereco_bairro.get(),
                               self.entry_endereco_municipio.get(),
                               self.entry_endereco_uf.get(),
                               self.entry_endereco_cep.get(),
                               self.entry_telefone_numero_1.get(),
                               self.entry_telefone_numero_2.get(),
                               self.entry_telefone_numero_3.get(),
                               self.entry_telefone_numero_4.get(),
                               self.entry_celular_numero_1.get(),
                               self.is_whatsapp.get(),
                               self.entry_email.get(),
                               self.entry_website.get(),
                               self.selected_pessoa_juridica
                               )
            db.update_pessoa_juridica(pessoa_juridica)
            messagebox.showinfo("Alerta", "Cadastro alterado com sucesso!")
        self.window.withdraw()
        self.confirm_callback()

    def __fill_pj(self, pj):
        self.__set_entry(self.entry_razao_social, pj['razao_social'])
        self.__set_entry(self.entry_nome_fantasia, pj['nome_fantasia'])
        self.__set_entry(self.entry_cnpj, pj['cnpj'])
        self.__set_entry(self.entry_inscricao_estadual, pj['inscricao_estadual'])
        self.__set_entry(self.entry_inscricao_municipal, pj['inscricao_municipal'])
        self.__set_entry(self.entry_endereco_complemento, pj['endereco_complemento'])
        self.__set_entry(self.entry_endereco_logradouro, pj['endereco_logradouro'])
        self.__set_entry(self.entry_endereco_bairro, pj['endereco_bairro'])
        self.__set_entry(self.entry_endereco_municipio, pj['endereco_municipio'])
        self.__set_entry(self.entry_endereco_uf, pj['endereco_uf'])
        self.__set_entry(self.entry_endereco_cep, pj['endereco_cep'])
        self.__set_entry(self.entry_telefone_numero_1, pj['telefone_numero_1'])
        self.__set_entry(self.entry_telefone_numero_2, pj['telefone_numero_2'])
        self.__set_entry(self.entry_telefone_numero_3, pj['telefone_numero_3'])
        self.__set_entry(self.entry_telefone_numero_4, pj['telefone_numero_4'])
        self.__set_entry(self.entry_celular_numero_1, pj['celular_numero_1'])
        self.__set_entry(self.entry_email, pj['email'])
        self.__set_entry(self.entry_website, pj['website'])
        self.__set_var(self.is_whatsapp, pj['celular_is_whatsapp_1'])

    def __set_entry(self, entry, value):
        entry.delete(0, tk.END)
        if value is not None:
            entry.insert(0, value)

    def __set_var(self, var, value, default_value=0):
        if value is None:
            var.set(default_value)
        else:
            var.set(value)

    def __clean_fields(self):
        entries = [
            self.entry_razao_social,
            self.entry_nome_fantasia,
            self.entry_cnpj,
            self.entry_inscricao_estadual,
            self.entry_inscricao_municipal,
            self.entry_endereco_logradouro,
            self.entry_endereco_complemento,
            self.entry_endereco_bairro,
            self.entry_endereco_municipio,
            self.entry_endereco_uf,
            self.entry_endereco_cep,
            self.entry_telefone_numero_1,
            self.entry_telefone_numero_2,
            self.entry_telefone_numero_3,
            self.entry_telefone_numero_4,
            self.entry_celular_numero_1,
            self.entry_email,
            self.entry_website,
        ]
        for entry in entries:
            entry.delete(0, tk.END)
        self.is_whatsapp.set(0)

###### FORMULARIO - ALTERACAO - FIM ###########################

###### MAIN - INICIO ##########################################

db = Database(
    user='root',
    password='password',
    host='localhost',
    database='cadastro'
)
db.connect()

main = tk.Tk()
main.title("Cadastro de Pessoa Jurídica")
form_pj = FormPessoaJuridica(
    db=db,
    parent=main,
    confirm_callback=None
)
list_pj = ListPessoaJuridica(
    db=db,
    parent=main,
    form_pj=form_pj
)
form_pj.confirm_callback = list_pj.load_tree
main.mainloop()
db.close()

###### MAIN - FIM #############################################
