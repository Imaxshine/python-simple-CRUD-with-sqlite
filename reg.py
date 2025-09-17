import db_conn as conn

# Register a new product
def RegisterProduct(Name:str, TakenBy:str, Quantity:int, Location:str, Price:int):
   try:
        connection = conn.GetConnection()
        cursor = connection.cursor()
    
        cursor.execute("INSERT INTO products (name, taken_by, quantity, location, price) VALUES (?, ?, ?, ?, ?)", (Name, TakenBy, Quantity, Location, Price))
   
        connection.commit()
        connection.close()
        print('New product were added')
   except Exception as error:
       print(f'Error: {error}')
        
def InsertUserInfo():
    print('''
          Inter the required credentials as mentioned below
          ''')
    try:
        Name = input('Product name > ')
        TakenBy = input('Taken by > ')
        Quantity = int(input('Product quantity > '))
        Location = input('Location to > ')
        Price = int(input('Product price > '))
        RegisterProduct(Name, TakenBy, Quantity, Location, Price)
    except ValueError as error:
        print(f'{error}')
        
InsertUserInfo()