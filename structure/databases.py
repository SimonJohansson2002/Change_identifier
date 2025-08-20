import mysql.connector

# Methods for databases using MySQL
# Make sure to initialize a database (mydb) and a cursor (mycursor)

# See README.md for how to start/stop database

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

def add_db(mycursor, name: str):
    """
    Adds a database if it does not exist. Does nothing if it exists.
    """
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")

def drop_db(mycursor, name: str):
    """
    Drops a database if it exists. Does nothing if it does not exist.
    """
    mycursor.execute(f"DROP DATABASE IF EXISTS {name}")

def show_dbs(mycursor):
    """
    Prints the names of the existing databases. 
    """
    mycursor.execute("SHOW DATABASES")

    for i in mycursor:
        print(i)