import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="",database="dbname")
mycursor=mydb.cursor()
mycursor.execute("select * from tablename");
for i in mycursor:
    print(i)
    