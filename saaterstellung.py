import sqlite3 as sql

def create(name, wachzeit, kornabstand, reihenabstand):
    sql = "INSERT INTO saat VALUES(name, wachszeit, kornabstand, reihenabstand)"
    cursor.execute(sql)
    connection.commit()