import mysql.connector

conn = mysql.connector.connect(host='localhost', database='friendsdb', user='root', password='*****')

if conn.is_connected():
    print("Connected to mysql friendsdb")

conn.close()