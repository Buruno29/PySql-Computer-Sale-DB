#this one is still manual

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="PC_Builders"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Customers (CustomerNumber INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Phone VARCHAR(255), Adress VARCHAR(255), Country VARCHAR(255))")
