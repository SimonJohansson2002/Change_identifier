import mysql.connector

# See README.md for how to start/stop database

# -------- Should make several python files, one for databases and one for tables. --------

# Databases -------------------------------------

def init_db(password: str):
    """
    Use this function if the database does not yet exist but will be added.
    """

    mydb = mysql.connector.connect(
        host="localhost",
        user="Simon",
        password=password)
    
    mycursor = mydb.cursor()

    return mydb, mycursor

def access_db(password: str, database: str):
    """
    Use this function if the database already exists.
    """

    mydb = mysql.connector.connect(
        host="localhost",
        user="Simon",
        password=password,
        database=database)
    
    mycursor = mydb.cursor()

    return mydb, mycursor

def add_db(name: str):
    """
    Adds a database if it does not exist. Does nothing if it exists.
    """
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")

def drop_db(name: str):
    """
    Drops a database if it exists. Does nothing if it does not exist.
    """
    mycursor.execute(f"DROP DATABASE IF EXISTS {name}")

def show_dbs():
    """
    Prints the names of the existing databases. 
    """
    mycursor.execute("SHOW DATABASES")

    for i in mycursor:
        print(i)

# Tables ----------------------------------------

def add_table(name: str, columns: list[str]):
    """
    Adds a table if it does not exist. Does nothing if it exists.

    Args:
        name (str): table name
        columns (list[str]): list of column names, should be larger than 1
    """
    cols = f'{columns[0]} VARCHAR(255)'

    if len(columns)<2:
        raise IndexError('Too few columns. Add at least 2 columns.')
    
    for col in columns[1:]:
        cols += f', {col} VARCHAR(255)'

    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({cols})")

def drop_table(name: str):
    """
    Drops a table if it exists. Does nothing if it does not exist.
    """
    mycursor.execute(f"DROP TABLE IF EXISTS {name}")

def show_tables():
    """
    Prints the names of the existing tables. The database must have been accessed through access_db.
    """

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

def insert(name: str, columns: list[str], val: list[tuple]):
    """
    Inserts list of tuples in a table. All tuples must equal dimension, larger than 0. 

    Args:
        name (str): name of the table to instert into
        columns (list[str]): list of column names
        val (list[tuple]): list of tuples, e.g. [(name1, address1, zip1, city1), (name2, address2, zip2, city2)]
    """
    
    num_columns = len(val[0])

    placeholders = ', '.join(['%s'] * num_columns)

    sql = f"INSERT INTO {name} VALUES ({placeholders})"

    mycursor.executemany(sql, val)
    mydb.commit()

def content_table(name: str, val=['*']):
    """
    Prints content in table in the current database. 

    Args:
        name (str): table name
        val (list, optional): list of columns or rows. Defaults to '*', i.e. the whole table.
    """

    columns = ', '.join(val)

    mycursor.execute(f"SELECT {columns} FROM {name}")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

if __name__=='__main__':
    #mydb, mycursor = init_db('jfyu_1&ofQnsp1^d6FJ')
    mydb, mycursor = access_db('jfyu_1&ofQnsp1^d6FJ', 'test')
    
    add_table('test_table1', ['name', 'age', 'size'])
    insert('test_table1', [('Simon', '23', '23cm'), ('Linus', '24', '12cm')])
    content_table('test_table1')
    
    #drop_table('test_table1')
    #show_tables()