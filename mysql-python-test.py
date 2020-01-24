#!/usr/bin/python3

'''
mysql-python-test

https://pynative.com/python-mysql-tutorial/

'''



import mysql.connector
from mysql.connector import Error


def main():
    try:
        connection = mysql.connector.connect(host='localhost', \
            database='SPLUNK_ONBOARDING', \
            user='root', \
            password='Password1!')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    sql_select_Query = "select * from environment_env"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in environment_env is: ", cursor.rowcount)

    print('ID====== Code=== Description==================== RCD==================== RLU================')
    for row in records:
        print(row[0], '\t', row[1], '\t',  row[2], '\t', row[3], '\t', row[4])


    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



if __name__ == "__main__":
    main()
