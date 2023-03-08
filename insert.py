import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO test1.test_table1 VALUES(123, 'prashant',456, 1.2,'hegde')")
mycursor.execute("INSERT INTO test1.test_table1 VALUES(123, 'prashant',456, 1.2,'hegde')")
mycursor.execute("INSERT INTO test1.test_table1 VALUES(123, 'prashant',456, 1.2,'hegde')")
mycursor.execute("INSERT INTO test1.test_table1 VALUES(123, 'prashant',456, 1.2,'hegde')")
mycursor.execute("INSERT INTO test1.test_table1 VALUES(123, 'prashant',456, 1.2,'hegde')")
mycursor.execute("INSERT INTO test1.test_table1 VALUES(123, 'prashant',456, 1.2,'hegde')")

mydb.commit()

mydb.close()