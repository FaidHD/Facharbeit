import sqlite3
import database as db


class create:
    def __init__(self, name, wachszeit, kornabstand, reihenabstand):

        self.con = db.Connection(
            hostname="db.faidhd.de",
            database="facharbeit",
            username="facharbeit",
            password="PhVS_-T0nNc7*K3]",
        )
        self.con.connect()

        self.name = name
        self.wachszeit = wachszeit
        self.kornabstand = kornabstand
        self.reihenabstand = reihenabstand
        self.saveData()

    def saveData(self):
        self.con.execute_stmt("INSERT INTO saat (name, wachszeit, kornabstand, reihenabstand) VALUES (?, ?, ?, ?)", (self.name, self.wachszeit, self.kornabstand, self.reihenabstand))
        self.con.close()
        return ("New seed added to Database")