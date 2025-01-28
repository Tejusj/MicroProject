import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="travelapp"
    )

    mycursor = mydb.cursor()

    # Show existing databases

    # Create table if not exists
    create_table_query = """CREATE TABLE IF NOT EXISTS USER (
                           USERID VARCHAR(20) PRIMARY KEY,
                           PASS VARCHAR(50),
                           NAME VARCHAR(50),
                           AGE INT NOT NULL,
                           MAIL VARCHAR(50)
                           )"""
    mycursor.execute(create_table_query)
    print("Table 'USER' created successfully.")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")
