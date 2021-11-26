import sqlite3
import os



def create(name, wachszeit, kornabstand, reihenabstand, connection, cursor):
    sql = "INSERT INTO saat VALUES(name, wachszeit, kornabstand, reihenabstand)"
    cursor.execute(sql)
    connection.commit()
    connection.close()