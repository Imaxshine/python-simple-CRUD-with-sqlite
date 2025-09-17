import db_conn as conn

def get_sum():
    connection = conn.GetConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(price) FROM products")
    total = cursor.fetchone()
    result = total[0]
    print("Total: ",format(result, ",.2f") + '/-',sep="")
get_sum()
