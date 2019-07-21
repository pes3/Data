import sqlite3

c = sqlite3.connect('test.db')
try:
    c.execute('''CREATE TABLE
                    mytable (Location        STRING,
                             Date            STRING,
                             Description     STRING)''')
except sqlite3.OperationalError: #i.e. table exists already
    pass
           
c.execute('''INSERT INTO mytable(Location, Date, Description) VALUES(?,?,?)''',
            ('test1', 'test2', 'test3'))
c.commit()
