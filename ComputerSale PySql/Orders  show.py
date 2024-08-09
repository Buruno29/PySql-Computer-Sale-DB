import mysql.connector
db = mysql.connector.connect(
     host='localhost',
     user="root",
     password="root",
     database = 'PC_Builders'
)

print(db)
print('===========================================')
print('Showing Compras:')
print('===========================================')
mycursor = db.cursor()

mycursor.execute("SELECT * FROM Orders")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)