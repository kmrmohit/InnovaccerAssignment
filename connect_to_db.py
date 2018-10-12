#connection to an existing mysql database is made
import mysql.connector
def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Km19982016",
        port="8081",
        database="testdb"
    )
    return mydb
