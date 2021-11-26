import os, sys, sqlite3
import saaterstellung as saE
import createDataBase as cDB


def SeedInput():
    name = input("Name: ")
    wachszeit = int(input("Wachszeit: "))
    kornabstand = int(input("Kornabstand: "))
    reihenabstand = int(input("Reihenabstand: "))
    saE.create(name, wachszeit, kornabstand, reihenabstand)


def sven():
    # Verbindung, Cursor
    connection = sqlite3.connect("Saatgut.db")
    cursor = connection.cursor()

    # SQL-Abfrage
    sql = "SELECT * FROM saat"

    cursor.execute(sql)

    # Ausgabe des Ergebnisses
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])

    # Verbindung beenden
    connection.close()
    print("Press Enter to continue!")
    input()
    start()

def start():
    print("Enter 1 to show currently saved seeds")
    print("Enter 2 to add a new seed to the Database")
    print("Enter 3 to delete the Database and create a new one")
    print("Enter 4 to quit program")
    command = int(input("Please Enter One of the Numbers: "))

    if command == 1:
        sven()
    elif command == 2:
        print(SeedInput())
        start()

    elif command == 3:
        try:
            os.remove("Saatgut.db")
        except:
            print("No old Database found, creating new one")
        cDB.Database()
        start()
    else:
        print("please Enter a Valid Number. Press Enter to try again.")
        input()


# Existenz feststellen
if os.path.exists("Saatgut.db"):
    print("Database already created!")
    start()
else:
    cDB.Database()
    start()


