#Esse infelizmente é manual eu acho

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="PC_Builders"
)

mycursor = db.cursor()
xid=input("Digite o Id do Produto:\n")
yquant=input("Nova quantidade")
sql = "UPDATE produto SET quantityInStock = %s WHERE produtoid = %s"
val = (xid, yquant)

mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record(s) affected")

