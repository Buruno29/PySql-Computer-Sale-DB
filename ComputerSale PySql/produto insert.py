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
        sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
        iname =input(print('Insira nome do produto:\n'))
        idesc =input(print('Insira a Descrição do Produto:\n'))
        iprice =input(print('Insira o Preço:\n'))
        istock =input(print('Insira a quantidade em estoque:\n'))
        val = (iname, idesc, iprice, istock) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")
    case "2":
        print("| 2 insert options chosen: |")
        print("1st:")
        sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
        iname =input(print('Insira nome do produto:\n'))
        idesc =input(print('Insira a Descrição do Produto:\n'))
        iprice =input(print('Insira o Preço:\n'))
        istock =input(print('Insira a quantidade em estoque:\n'))
        val = (iname, idesc, iprice, istock) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")

        print("2nd:")
        sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
        iname =input(print('Insira nome do produto:\n'))
        idesc =input(print('Insira a Descrição do Produto:\n'))
        iprice =input(print('Insira o Preço:\n'))
        istock =input(print('Insira a quantidade em estoque:\n'))
        val = (iname, idesc, iprice, istock) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")


    case "3":
        for a in range(3):
           print(a)
           sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
           iname =input(print('Insira nome do produto:\n'))
           idesc =input(print('Insira a Descrição do Produto:\n'))
           iprice =input(print('Insira o Preço:\n'))
           istock =input(print('Insira a quantidade em estoque:\n'))
           val = (iname, idesc, iprice, istock) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")

    
    case "4":
        for a in range(4):
           print(a)
           sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
           iname =input(print('Insira nome do produto:\n'))
           idesc =input(print('Insira a Descrição do Produto:\n'))
           iprice =input(print('Insira o Preço:\n'))
           istock =input(print('Insira a quantidade em estoque:\n'))
           val = (iname, idesc, iprice, istock) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")

    case "5":
        for a in range(5):
           print(a)
           sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
           iname =input(print('Insira nome do produto:\n'))
           idesc =input(print('Insira a Descrição do Produto:\n'))
           iprice =input(print('Insira o Preço:\n'))
           istock =input(print('Insira a quantidade em estoque:\n'))
           val = (iname, idesc, iprice, istock) #dados da função
           mycursor.execute(sql, val)

           db.commit()
           print(mycursor.rowcount, "record inserted.")
    case _:
        print("| 1 insert option chosen: |")
        sql = "INSERT INTO Products (Name, Description, Price, Qtstock) VALUES (%s, %s, %s, %s)" #função
        iname =input(print('Insira nome do produto:\n'))
        idesc =input(print('Insira a Descrição do Produto:\n'))
        iprice =input(print('Insira o Preço:\n'))
        istock =input(print('Insira a quantidade em estoque:\n'))
        val = (iname, idesc, iprice, istock) #dados da função
        mycursor.execute(sql, val)

        db.commit()
        print(mycursor.rowcount, "record inserted.")

