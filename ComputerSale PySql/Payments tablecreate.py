#this one is still manual

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="PC_Builders"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Payments (CheckNumber INT PRIMARY KEY, CustomerNumber INT, PaymentDate DATE, Amount INT, FOREIGN KEY (CustomerNumber) references Customers(CustomerNumber))")