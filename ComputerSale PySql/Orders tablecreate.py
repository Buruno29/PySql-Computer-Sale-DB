#this one is still manual

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="PC_Builders"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Orders (OrderNumber INT AUTO_INCREMENT PRIMARY KEY, OrderDate DATE, RequiredDate DATE, ShippedDate DATE, Status VARCHAR(255), Comments VARCHAR(255), CustomerNumber INT)")
