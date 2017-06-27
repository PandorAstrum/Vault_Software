# responsible for database queries

import sqlite3 as lite
import sys

con = None

def Create_database():
    try:
        con = lite.connect("vault.db")
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

    except lite.Error as e:
        print("Error {1}", e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()


def Set_data():
    pass

def Get_Data():
    pass


Create_database()