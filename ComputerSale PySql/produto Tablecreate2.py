#this one is still manual

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="PC_Builders"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Products (ProductCode INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Description VARCHAR(255), Qtstock INT, Price INT)")

