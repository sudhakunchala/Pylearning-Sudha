# insert update delete
import mysql.connector

insert_query="insert into stu1 values(102,'Akki',25)"
update_query="update stu1 set sname='Arjun' where sno=100"
delete_query="delete from stu1 where sno=102"

#to establish connection ,we need to give below details:
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
cur=con.cursor()
cur.execute(delete_query) # execute query through cursor
con.commit() # commit transaction
con.close()

print("Finished....")
