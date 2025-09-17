import db_conn as conn
from read import ReadData as SomaData

def DeleteData(product_id:int):
    try:
        connection = conn.GetConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        # IF QUERY SUCCESS TO EXECUTE
        connection.commit()
        print('Product were deleted successfully')
        SomaData()
    except Exception as e:
        print(f'Error: {e}')
        
    finally:
        connection.close()
        
def UserDeleteProduct():
    print('\n Select product to delete from above')
    print('-------------------------------------')
    try:
        Id = int(input('Enter the product id to delete. > '))
        DeleteData(Id)
    except ValueError:
        print('Invalid id product were detected!')
UserDeleteProduct()
    