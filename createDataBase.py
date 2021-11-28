import sqlite3


class Database:
    def __init__(self):
        # Verbindung zur Datenbank erzeugen
        self.connection = sqlite3.connect("Saatgut.db")

        # Datensatz-Cursor erzeugen
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        print("creating table")
        # Datenbanktabelle erzeugen
        self.sql = "CREATE TABLE saat(name TEXT PRIMARY KEY, wachszeit INTEGER NOT NULL, kornabstand INTEGER NOT NULL, reihenabstand INTEGER NULL)"
        self.cursor.execute(self.sql)
        self.connection.close()

