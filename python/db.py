#import pymysql.cursors
#import os
import mysql

def connect():
    #return pymysql.connect(host=os.environ['DB_HOST'],
    #                             user=os.environ['DB_USER'],
    #                             password=os.environ['DB_PASSWORD'],
    #                             db=os.environ['DB_DATABASE'],
    #                             charset='utf8',
    #                             cursorclass=pymysql.cursors.DictCursor)

    cnx = mysql.connector.connect(user='scott', password='password',
                                  host='127.0.0.1',
                                  database='employees')
    cnx.close()

def insert_sales():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `sales` (date, floatDate, account, amount) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('2019-03-15', '2019-03-15', '123', 99))
        connection.commit()

    finally:
        connection.close()

def select_sales():
    connection = connect()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)