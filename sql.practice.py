import sqlite3

def run_query(query , params=()):
    connection = sqlite3.connect("practice.db")
    cursor = connection.cursor()
    cursor.execute(query , params)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()
    connection.close()


run_query("select * from medicines where name like '%mo%'")