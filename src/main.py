#!/usr/bin/env python3

import sys

import mysql.connector

from tkinter import messagebox

from ClientList import *
from Database import Database

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

