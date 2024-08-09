#this one is still manual

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE PC_Builders")
