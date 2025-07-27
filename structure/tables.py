import mysql.connector

# Methods for tables using MySQL
# Make sure to initialize a database (mydb) and a cursor (mycursor)

# See README.md for how to start/stop database

# Tables -------------------------------------

def add_table(table: str, columns: list[str]):
    """
    Adds a table if it does not exist. Does nothing if it exists.

    Args:
        table (str): table name
        columns (list[str]): list of column names, should be larger than 1
    """
    cols = f'{columns[0]} VARCHAR(255)'

    if len(columns)<2:
        raise IndexError('Too few columns. Add at least 2 columns.')
    
    for col in columns[1:]:
        cols += f', {col} VARCHAR(255)'

    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({cols})")

def drop_table(table: str):
    """
    Drops a table if it exists. Does nothing if it does not exist.
    """
    mycursor.execute(f"DROP TABLE IF EXISTS {table}")

def show_tables():
    """
    Prints the names of the existing tables. The database must have been accessed through access_db.
    """

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

def insert(table: str, val: list[tuple]):
    """
    Inserts list of tuples in a table. All tuples must equal dimension, larger than 0. 

    Args:
        table (str): name of the table to instert into
        columns (list[str]): list of column names
        val (list[tuple]): list of tuples, e.g. [(name1, address1, zip1, city1), (name2, address2, zip2, city2)]
    """
    
    num_columns = len(val[0])

    placeholders = ', '.join(['%s'] * num_columns)

    sql = f"INSERT INTO {table} VALUES ({placeholders})"

    mycursor.executemany(sql, val)
    mydb.commit()

def content_table(table: str, columns=['*']):
    """
    Prints content in table in the current database. 

    Args:
        table (str): table name
        columns (list, optional): list of columns or rows. Defaults to '*', i.e. the whole table.
    """

    columns = ', '.join(columns)

    mycursor.execute(f"SELECT {columns} FROM {table}")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def print_specific(table: str, column: str, val):
    """
    Prints all rows in the table whith a specific value in a given column. 

    Args:
        table (str): table name
        column (str): column name
        val (_type_): specific value to look for, type depends on what it was inserted as
    """

    sql = f"SELECT * FROM {table} WHERE {column} = %s"
    val = (val, )

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def print_sorted(table: str, column: str, order: int=0):
    """
    Prints table ordered in ascending (default) or descending order by chosen column. 

    Args:
        table (str): table name
        column (str): column name to order by
        order (int, optional): 0 sorts in ascending order. 1 sorts in descending order. Defaults to 0.
    """
    if order == 0:
        sql = f"SELECT * FROM {table} ORDER BY {column}"
    elif order == 1:
        sql = f"SELECT * FROM {table} ORDER BY {column} DESC"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def delete_rows(table: str, column: str, val):
    """
    Deletes all rows in the table whith a specific value in a given column.

    Args:
        table (str): table name
        column (str): column name
        val (_type_): specific value to delete
    """
    sql = f"DELETE FROM {table} WHERE {column} = %s"
    val = (val, )

    mycursor.execute(sql, val)

    mydb.commit()

def unique_update(table: str, id_column: str, id, update_column: str, new_value):
    """
    Updates value an existing column in an existing row. 

    Args:
        table (str): table name
        id_column (str): column name containg unique values
        id (_type_): unique value (works with non-unique)
        update_column (str): column name containg the value to be updated
        new_value (_type_): value to be updated to
    """

    sql = f"UPDATE {table} SET {update_column} = %s WHERE {id_column} = %s"
    val = (new_value, id)
    mycursor.execute(sql, val)

def print_limited_rows(table: str, limit: int, offset: int=0):
    """
    Prints a limited number of rows, ignoring a given number of rows.

    Args:
        table (str): table name
        limit (int): number of rows to print
        offset (int, optional): rows ignored before printing. Defaults to 0.
    """

    if offset == 0:
        limit = str(limit)
        offset = str(offset)
        mycursor.execute(f"SELECT * FROM {table} LIMIT {limit}")
    elif offset > 0:
        limit = str(limit)
        offset = str(offset)
        mycursor.execute(f"SELECT * FROM {table} LIMIT {limit} OFFSET {offset}")
    
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def join():
    """
    Might need later
    """
    return