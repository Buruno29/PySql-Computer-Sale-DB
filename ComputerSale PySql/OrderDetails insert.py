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
        sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber) VALUES (%s, %s, %s, %s, %s)" #função
        inumber =input(print('Insira o Numero da Ordem Existente:\n'))
        iprodcod =input(print('Insira o Código do Produto Existente:\n'))
        iqt=input(print('Insira a quantidade pedida:\n'))
        ioprice=input(print('Insira o preço do Pedido:\n'))
        iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
        
        val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")

    case "2":
        print("| 2 insert options chosen: |")
        print("1st:")
        sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber) VALUES (%s, %s, %s, %s, %s)" #função
        inumber =input(print('Insira o Numero da Ordem Existente:\n'))
        iprodcod =input(print('Insira o Código do Produto Existente:\n'))
        iqt=input(print('Insira a quantidade pedida:\n'))
        ioprice=input(print('Insira o preço do Pedido:\n'))
        iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
        
        val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")
        print("2nd:")
        sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber) VALUES (%s, %s, %s, %s, %s)" #função
        inumber =input(print('Insira o Numero da Ordem Existente:\n'))
        iprodcod =input(print('Insira o Código do Produto Existente:\n'))
        iqt=input(print('Insira a quantidade pedida:\n'))
        ioprice=input(print('Insira o preço do Pedido:\n'))
        iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
        
        val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função
        mycursor.execute(sql, val)


        db.commit()
        print(mycursor.rowcount, "record inserted.")


    case "3":
        for a in range(3):
           print(a)
           sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber) VALUES (%s, %s, %s, %s, %s)" #função
           inumber =input(print('Insira o Numero da Ordem Existente:\n'))
           iprodcod =input(print('Insira o Código do Produto Existente:\n'))
           iqt=input(print('Insira a quantidade pedida:\n'))
           ioprice=input(print('Insira o preço do Pedido:\n'))
           iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
           
           val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função

           db.commit()
           print(mycursor.rowcount, "record inserted.")

    
    case "4":
        for a in range(4):
           print(a)
           sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber) VALUES (%s, %s, %s, %s, %s)" #função
           inumber =input(print('Insira o Numero da Ordem Existente:\n'))
           iprodcod =input(print('Insira o Código do Produto Existente:\n'))
           iqt=input(print('Insira a quantidade pedida:\n'))
           ioprice=input(print('Insira o preço do Pedido:\n'))
           iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
           
           val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")

    case "5":
        for a in range(5):
           print(a)
           sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber, ProductCode) VALUES (%s, %s, %s, %s, %s, %s)" #função
           inumber =input(print('Insira o Numero da Ordem Existente:\n'))
           iprodcod =input(print('Insira o Código do Produto Existente:\n'))
           iqt=input(print('Insira a quantidade pedida:\n'))
           ioprice=input(print('Insira o preço do Pedido:\n'))
           iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
           
           val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")
    case _:
        print("| 1 insert option chosen: |")
        sql = "INSERT INTO Orderdetails (OrderNumber, ProductCode, Qtordered, PriceEach, OrderLineNumber) VALUES (%s, %s, %s, %s, %s)" #função
        inumber =input(print('Insira o Numero da Ordem Existente:\n'))
        iprodcod =input(print('Insira o Código do Produto Existente:\n'))
        iqt=input(print('Insira a quantidade pedida:\n'))
        ioprice=input(print('Insira o preço do Pedido:\n'))
        iOLN=input(print('Insira o Número da Ordem na Fila:\n'))
        
        val = (inumber, iprodcod ,  iqt, ioprice, iOLN) #dados da função
        mycursor.execute(sql, val)
        db.commit()       
        print(mycursor.rowcount, "record inserted.")
