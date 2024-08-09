import mysql.connector
db = mysql.connector.connect(
     host='localhost',
     user="root",
     password="root",
     database = 'PC_Builders'
)

print(db)
print('===========================================')
print('Showing Produto:')
print('===========================================')
mycursor = db.cursor()

mycursor.execute("SELECT * FROM Products")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
