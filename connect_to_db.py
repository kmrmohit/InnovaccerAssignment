#connection to an existing mysql database is made
import mysql.connector
def connect():
    mydb = mysql.connector.connect(
        host="localhost", #specifies the server address where your database is running
        user="root",      #username for accessing database
        password="1234",  #password for accessing database
        port="8081",      #port no of your server
        database="testdb" #name of your database"
    )
    return mydb
