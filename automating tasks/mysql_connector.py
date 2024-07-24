import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bulacia",
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE JUSTPROVING")
# mycursor.execute("USE JUSTPROVING")
