import db_conn as conn
import read as somaData

def UpdateData(product_id:int, name, takenBy, quantity:int, location, price:int):
    try:
        connection = conn.GetConnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET name = ?, taken_by = ?, quantity = ?, location = ?, price = ? WHERE id = ?",
                                   (name, takenBy, quantity, location, price, product_id))
        """
            Onesha Update mpya kwa sasa
        """
        connection.commit()
        print('\n Update successfully \n')
        
        """
             Onesha Orodha mpya iliyo sasishwa upya
        """
        somaData.ReadData()
    except Exception as error:
        print(f'Something wrong with Update: {error}')
    finally:
        connection.close()
        
def UserUpdateInputs():
    try:
        print('''
             UPDATE DATA 
              ''')
        product_id = int(input('Enter a product Id: > '))
        Name = input('New Product name: > ')
        TakenBy = input('New taken by: > ')
        Quantity = int(input('New Quantity: > '))
        Location = input('New location: > ')
        Price = int(input('New price: > '))
        
        """
            Ita method ya ku update data na tia parameter zake zote
        """
        
        UpdateData(product_id, Name, TakenBy, Quantity, Location, Price)
    except Exception as error:
        print(f'Errors: {error}')
        
UserUpdateInputs()
    