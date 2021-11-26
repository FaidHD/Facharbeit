import sqlite3
import os



def create(name, wachszeit, kornabstand, reihenabstand):
    if os.path.exists("Saatgut.db"):
        # Verbindung zur Datenbank erzeugen
        connection = sqlite3.connect("Saatgut.db")

        # Datensatz-Cursor erzeugen
        cursor = connection.cursor()

    sql = "INSERT INTO saat VALUES(name, wachszeit, kornabstand, reihenabstand)"
    cursor.execute(sql)
    connection.commit()
    connection.close()