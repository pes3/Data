#using sqllite
import sqlite3
## Create Connection and table file

c = sqlite3.connect('weather.db')

## Create table
try: ## if a table already existis, and you execute a create table an operational error will be thrown because it's trying to create another table that alrady exists(adding a new column after running could pose issue, essentially you have to delete db file and recreate it with new colum)
    c.execute('''CREATE TABLE mytable (
  id 		INTEGER PRIMARY KEY,
  number 	INTEGER,
  T             Date            )''');
except sqlite3.OperationalError: #i.e. table exists already
    pass
c.execute('''INSERT INTO mytable (number, t) VALUES(20,DATE('now'))''')
c.execute('''
INSERT INTO mytable (number, t) VALUES(23,DATE('now'))''')

#commit to the db, so this it when is saves/stores the to insert statements above
c.commit()

rs = c.execute('Select * FROM mytable') # show what is currently inside DB
#for result in rs:
    #print(result) - comment this out because we need to iterate over late
## using DB Brower for SQlite to view my data
## now save as csv file

'''with open('test.csv', 'w') as f: # trying to make a csv file, put on ice
    for result in rs:
       f.write(str(result))
        print(str(result))'''    # going to put this on ice till full works
## keep in mind this option - look into
#df = pd.read_sql_query("SELECT * FROM table_name", cnx)

