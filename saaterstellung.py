import sqlite3
import os


class create:
    def __init__(self, name, wachszeit, kornabstand, reihenabstand):
        connection = sqlite3.connect("Saatgut.db")
        cursor = connection.cursor()
        self.name = name
        self.wachszeit = wachszeit
        self.kornabstand = kornabstand
        self.reihenabstand = reihenabstand
        self.connection = connection
        self.cursor = cursor
        self.saveData()

    def saveData(self):
        self.cursor.execute("INSERT INTO saat (name, wachszeit, kornabstand, reihenabstand) VALUES (?, ?, ?, ?)", (self.name, self.wachszeit, self.kornabstand, self.reihenabstand))
        self.connection.commit()
        self.connection.close()
        return ("New seed added to Database")