import sqlite3 as sql

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("Saatgut.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

def create(name, wachzeit, kornabstand, reihenabstand):
    sql = "INSERT INTO saat VALUES(name, wachszeit, kornabstand, reihenabstand)"
    cursor.execute(sql)
    connection.commit()
    connection.close()