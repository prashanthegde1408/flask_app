import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT c1,c2 FROM test1.test_table1")

for x in mycursor.fetchall():
    print(x)

mydb.close()