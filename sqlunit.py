import sqlite3

c = sqlite3.connect('test.db')

def create_table():
    try:
        c.execute('''CREATE TABLE
                    mytable (Location        STRING,
                             Date            STRING,
                             Description     STRING)''')
    except sqlite3.OperationalError: #i.e. table exists already
        pass


def insert_table(value1, value2, value3):
    c.execute('''INSERT INTO mytable(Location, Date, Description) VALUES(?,?,?)''',
            (value1, value2, value3))
    c.commit()
#essnetially creating DAO - data access object, a layer between DB & code

def count_rows():
    #execute sql query
    cursor = c.cursor()
    cursor.execute('''SELECT * FROM mytable;''')
    results = cursor.fetchall()
    return len(results)
