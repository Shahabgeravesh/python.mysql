# connect to mysql database
from mysql.connector import (connection)
mydb = connection.MySQLConnection(user='root', password='Shahab1373!!',
                                  host='localhost',
                                  database='dashboard_db')
# create a new database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# show all the databases
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
