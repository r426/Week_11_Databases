import mysql.connector

conn = mysql.connector.connect(host='localhost', database='friendsdb', user='root', password='*****')

if conn.is_connected():
    print("Connected to mysql friendsdb")

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE tourneys(id int, name varchar(30), wins int, best int, size int);")
    conn.commit()
    print('Table "tourneys" created.')
except:
    conn.rollback()

cursor.close()
conn.close()

conn.close()