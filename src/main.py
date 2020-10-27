#!/usr/bin/env python3

#Definir usuário e senha para acessar o banco de dados abaixo:
USER = 'dev'
PASSWORD = 'dev'

from ClientList import *
from Database import Database

def main():
    db = Database(USER, PASSWORD, 'localhost', 'sci_db')
    instance_list = ClientList(db)
    instance_list.mainloop()
    db.close()

if __name__ == "__main__":
    main()

