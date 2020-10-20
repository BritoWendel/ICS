#!/usr/bin/env python3

from ClientList import *
from Database import Database

def main():
    db = Database('root', 'test', 'localhost', 'sci_db')
    instance_list = ClientList(db)
    instance_list.mainloop()
    db.close()

if __name__ == "__main__":
    main()

