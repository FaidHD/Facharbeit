import os, sys, sqlite3
import saaterstellung as saE

def sven():
    input("Please Press Enter to continue!")


    # Verbindung, Cursor
    connection = sqlite3.connect("Saatgut.db")
    cursor = connection.cursor()

    # SQL-Abfrage
    sql = "SELECT * FROM saat"

    # Kontrollausgabe der SQL-Abfrage
    print(sql)

    # Absenden der SQL-Abfrage
    # Empfang des Ergebnisses
    cursor.execute(sql)

    # Ausgabe des Ergebnisses
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])

    # Verbindung beenden
    connection.close()
    sys.exit(0)
    
# Existenz feststellen
if os.path.exists("Saatgut.db"):
    print("Datei bereits vorhanden")
    sven()

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("Saatgut.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Datenbanktabelle erzeugen
sql = "CREATE TABLE saat(" \
      "name TEXT PRIMARY KEY, " \
      "wachszeit INTEGER NOT NULL, " \
      "kornabstand INTEGER NOT NULL, " \
      "reihenabstand INTEGER NULL)"
cursor.execute(sql)

# Datensatz erzeugen
sql = "INSERT INTO saat VALUES('Mais', 16, 10, 60)"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
#sql = "INSERT INTO saat VALUES('Weizen', 4, 22, 22)"
#cursor.execute(sql)
#connection.commit()

name = input("Name: ")
wachszeit = input("Wachszeit: ")
kornabstand = input("Kornabstand: ")
reihenabstand = input("Reihenabstand: ")
saE.create(name, wachszeit, kornabstand, reihenabstand)


# Verbindung beenden
connection.close()