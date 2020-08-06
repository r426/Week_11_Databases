import mysql.connector

conn = mysql.connector.connect(host='localhost', database='friendsdb', user='root', password='*****')

if conn.is_connected():
    print("Connected to mysql friendsdb")

cursor = conn.cursor()

try:
    # cursor.execute("CREATE TABLE tourneys(id int, name varchar(20), wins int, best int, size int);")
    cursor.execute("INSERT INTO tourneys values(1, 'John', 10, 240, 40);")
    cursor.execute("INSERT INTO tourneys values(2, 'Adda', 12, 140, 39);")
    cursor.execute("INSERT INTO tourneys values(3, 'Lynn', 8, 200, 38);")
    cursor.execute("INSERT INTO tourneys values(4, 'Roy', 14, 240, 42);")
    cursor.execute("INSERT INTO tourneys values(5, 'Tom', 9, 100, 41);")
    cursor.execute("INSERT INTO tourneys values(6, 'Jake', 10, 160, 40);")
    conn.commit()
except:
    conn.rollback()

cursor.execute('SELECT * FROM tourneys')
rows = cursor.fetchall()
print("Total Number of records", cursor.rowcount)

for row in rows:
    print(row)

try:
    cursor.execute(
        "CREATE TABLE favorite_meals(id int, name varchar(20), birth_month varchar(10),"
        " birth_day int, entree varchar(20), side varchar(20), dessert varchar(20));")
    cursor.execute("INSERT INTO favorite_meals values(1, 'John', 'January', 16, 'dumplings', 'asparagus', 'cupcakes');")
    cursor.execute("INSERT INTO favorite_meals values(2, 'Adda', 'March', 10, 'bocconcini', 'broccoli', 'donuts');")
    cursor.execute("INSERT INTO favorite_meals values(3, 'Lynn', 'February', 18, 'salmon', 'cabbage', 'eclairs');")
    cursor.execute("INSERT INTO favorite_meals values(4, 'Roy', 'May', 24, 'noodles', 'cauliflower', 'froyo');")
    cursor.execute("INSERT INTO favorite_meals values(5, 'Tom', 'May', 19, 'seafood', 'greens', 'gingerbread');")
    cursor.execute("INSERT INTO favorite_meals values(6, 'Jake', 'July', 11, 'rolls', 'mushrooms', 'marshmellow');")
    conn.commit()
except:
    conn.rollback()

cursor.execute('SELECT * FROM favorite_meals')
rows = cursor.fetchall()
print("Total Number of records", cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()

conn.close()
