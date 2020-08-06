import mysql.connector

conn = mysql.connector.connect(host='localhost', database='friendsdb', user='root', password='*****')

if conn.is_connected():
    print("Connected to mysql friendsdb")

cursor = conn.cursor()

try:
    # cursor.execute("CREATE TABLE tourneys(id int, name varchar(30), wins int, best int, size int);")
    cursor.execute("INSERT INTO tourneys values(1, 'John', 10, 240, 40);")
    cursor.execute("INSERT INTO tourneys values(2, 'Adda', 12, 140, 39);")
    cursor.execute("INSERT INTO tourneys values(3, 'Lynn', 8, 200, 38);")
    cursor.execute("INSERT INTO tourneys values(4, 'Roy', 14, 240, 42);")
    cursor.execute("INSERT INTO tourneys values(5, 'Tom', 9, 100, 41);")
    cursor.execute("INSERT INTO tourneys values(6, 'Jake', 10, 160, 40);")
    cursor.execute("INSERT INTO tourneys values(7, 'Rose', 11, 210, 37);")
    cursor.execute("INSERT INTO tourneys values(8, 'Ted', 7, 180, 40);")
    cursor.execute("INSERT INTO tourneys values(9, 'Jeff', 9, 120, 40);")
    cursor.execute("INSERT INTO tourneys values(10, 'Sue', 15, 270, 38);")
    conn.commit()
except:
    conn.rollback()

cursor.execute('SELECT * FROM tourneys')
rows = cursor.fetchall()
print("Total Number of records", cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()

conn.close()