import sqlite3

def run_query(query):
    connection =sqlite3.connect("students_practice.db")
    cursor=connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows :
        print(row)
    connection.commit()
    connection.close()

run_query("""
    create table if not exists students(
        id integer primary key autoincrement,
        name text,
        age integer,
        score integer
    )
""")

run_query("select * from students order by age limit 3")
