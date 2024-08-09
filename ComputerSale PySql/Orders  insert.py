import mysql.connector
db = mysql.connector.connect(
     host='localhost',
     user="root",
     password="root",
     database = 'PC_Builders'
)

mycursor = db.cursor()

insertamount = input("How many do you want to insert? (1-5)")

match insertamount:
    case "1":
        print("| 1 insert option chosen: |")
        sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
        iname =input(print('Insira o Numero do Cliente:\n'))
        icomment =input(print('Insira Comentário:\n'))
        istat=input(print('Insira Status da Ordem:\n'))
        iorderdate=input(print('Insira a Data da Ordem:\n'))
        irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
        ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
        val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")

    case "2":
        print("| 2 insert options chosen: |")
        print("1st:")
        sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
        iname =input(print('Insira o Numero do Cliente:\n'))
        icomment =input(print('Insira Comentário:\n'))
        istat=input(print('Insira Status da Ordem:\n'))
        iorderdate=input(print('Insira a Data da Ordem:\n'))
        irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
        ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
        val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")
        print("2nd:")
        sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
        iname =input(print('Insira o Numero do Cliente:\n'))
        icomment =input(print('Insira Comentário:\n'))
        istat=input(print('Insira Status da Ordem:\n'))
        iorderdate=input(print('Insira a Data da Ordem:\n'))
        irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
        ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
        val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função
        mycursor.execute(sql, val)


        db.commit()
        print(mycursor.rowcount, "record inserted.")


    case "3":
        for a in range(3):
           print(a)
           sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
           iname =input(print('Insira o Numero do Cliente:\n'))
           icomment =input(print('Insira Comentário:\n'))
           istat=input(print('Insira Status da Ordem:\n'))
           iorderdate=input(print('Insira a Data da Ordem:\n'))
           irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
           ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
           val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função

           db.commit()
           print(mycursor.rowcount, "record inserted.")

    
    case "4":
        for a in range(4):
           print(a)
           sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
           iname =input(print('Insira o Numero do Cliente:\n'))
           icomment =input(print('Insira Comentário:\n'))
           istat=input(print('Insira Status da Ordem:\n'))
           iorderdate=input(print('Insira a Data da Ordem:\n'))
           irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
           ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
           val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")

    case "5":
        for a in range(5):
           print(a)
           sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
           iname =input(print('Insira o Numero do Cliente:\n'))
           icomment =input(print('Insira Comentário:\n'))
           istat=input(print('Insira Status da Ordem:\n'))
           iorderdate=input(print('Insira a Data da Ordem:\n'))
           irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
           ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
           val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")
    case _:
        print("| 1 insert option chosen: |")
        sql = "INSERT INTO Orders (CustomerNumber, Comments, Status, OrderDate, RequiredDate, ShippedDate) VALUES (%s, %s, %s, %s, %s, %s)" #função
        iname =input(print('Insira o Numero do Cliente:\n'))
        icomment =input(print('Insira Comentário:\n'))
        istat=input(print('Insira Status da Ordem:\n'))
        iorderdate=input(print('Insira a Data da Ordem:\n'))
        irequireddate=input(print('Insira a Data de previsão de chegada:\n'))
        ishippeddate=input(print('Insira a Data em que foi Exportada:\n'))
        val = (iname, icomment, istat, iorderdate, irequireddate, ishippeddate) #dados da função
        mycursor.execute(sql, val)
        db.commit()       
        print(mycursor.rowcount, "record inserted.")
