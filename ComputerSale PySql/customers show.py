import mysql.connector
db = mysql.connector.connect(
     host='localhost',
     user="root",
     password="root",
     database = 'PC_Builders'
)

print(db)
print('===========================================')
print('Showing Customers:')
print('===========================================')
mycursor = db.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
