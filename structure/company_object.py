import mysql.connector

#See README.md for how to start/stop database

def init_db(password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="Simon",
        password=password)

    mycursor = mydb.cursor()

    return mydb, mycursor

def add_db(name):
    mycursor.execute(f"CREATE DATABASE {name}")

def drop_db(name):
    mycursor.execute(f"DROP DATABASE IF EXISTS {name}")

def show_dbs():
    mycursor.execute("SHOW DATABASES")

    for i in mycursor:
        print(i)

def check_company(name):
    pass

if __name__=='__main__':
    mydb, mycursor = init_db('jfyu_1&ofQnsp1^d6FJ')