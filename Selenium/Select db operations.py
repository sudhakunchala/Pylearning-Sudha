# insert update delete
import mysql.connector

#to establish connection ,we need to give below details:
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
cur=con.cursor()
cur.execute("select * from orders") # execute query through cursor
for row in cur:
    print(row[0],row[1],row[2])
con.close()

print("Finished....")
