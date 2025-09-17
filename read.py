import db_conn as conn
# from total import get_sum as total

def ReadData():
    connection = conn.GetConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    # Tuna loop data kwa kutumia for() Loop
    for row, result in enumerate(results, 1):
        Id, name, taken, quantity, location, price = result
        print(f'{row} -> {Id}: Product Name {name}, Taken by {taken}, Quantity {quantity}, Location {location} and price is {price:,}/-' + '\n')

    # Onesha Jumla
    import total
    connection.commit()
    connection.close()
ReadData()