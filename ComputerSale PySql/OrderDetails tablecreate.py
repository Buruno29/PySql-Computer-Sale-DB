#this one is still manual

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="PC_Builders"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Orderdetails (OrderNumber INT, ProductCode INT, Qtordered INT, PriceEach INT,  OrderLineNumber INT, PRIMARY KEY (OrderNumber, ProductCode), FOREIGN KEY (OrderNumber) references Orders(OrderNumber), FOREIGN KEY (ProductCode) references Products(ProductCode) );")