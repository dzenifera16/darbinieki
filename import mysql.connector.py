import mysql.connector

try:
    connection = mysql.connector.connect(host='remotemysql.com', 
                                         database='9AcrXRUMyJ',
                                         user='9AcrXRUMyJ',
                                         password='l3693iW5Dx')

    sql_select_Query = "select * from darbinieki"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("ID = ", row[0], )
        print("Vārds = ", row[1])
        print("Uzvārds  = ", row[2])
        print("Vecums = ", row[3], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")