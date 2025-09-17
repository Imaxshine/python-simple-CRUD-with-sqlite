import sqlite3

def GetConnection():
    conn = sqlite3.connect('biashara.db')
    if conn:
        # print('Db created')
        return conn
    else:
        return 'Connection error'

# Create table products
def CreateTable():
    conn = GetConnection()
    cursor = conn.cursor()
    ProductTable = cursor.execute('''
                 CREATE TABLE IF NOT EXISTS products 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 taken_by TEXT,
                 quantity INTEGER,
                 location TEXT,
                 price INTEGER
                 )
                 ''')
    conn.commit()
    conn.close()

CreateTable()
    