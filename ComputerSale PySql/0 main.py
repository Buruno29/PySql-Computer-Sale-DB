import mysql.connector
db = mysql.connector.connect(
     host='localhost',
     user="root",
     password="root",
     database = 'PC_Builders'
)

print(db)
print('===========================================')
print("Database Initiated")
print('===========================================')
mycursor = db.cursor()
print("Available actions:")
print("1- Show All Tables \n2- All Purchase Results\n3- All Products\n")
action = input("What do you want to do? \n ")
match action:
    case "1":
      mycursor.execute("SHOW TABLES")

      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)

    case "2":
      SQL = ("SELECT Customers.Name AS cliente, Products.Name AS produto, Products.Description AS descrição\
      FROM Customers\
      INNER JOIN Orders ON Orders.CustomerNumber = Customers.CustomerNumber\
      INNER JOIN OrderDetails ON OrderDetails.OrderNumber = Orders.Ordernumber\
      INNER JOIN Products ON Products.ProductCode = OrderDetails.ProductCode\
      WHERE Products.ProductCode < 3")
      mycursor.execute(SQL)
      myresult = mycursor.fetchall()

      for x in myresult:
        print(x)
    case "3":
      SQL2 = ("SELECT * FROM Products")
      mycursor.execute(SQL2)
      myresult = mycursor.fetchall()
      for x in myresult:
        print(x)      
    



