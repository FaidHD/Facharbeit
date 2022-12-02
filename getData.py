import main
import createOutput as cO


class GetData:

    def __init__(self):
        self.avSpeed = None
        self.fuelUsage = None
        self.seed = ""
        self.name = ""
        self.grow_time = ""
        self.seed_space = ""
        self.row_space = ""
        self.result = []
        self.height = []
        self.width = []

    def seedData(self):
        cO.Output([
                      "Bitte gib den Namen der Kornart an, die du anlegen möchtest"]).printString()  # Welche Daten sind gebraucht
        self.name = input("» ")  # Warten auf entsprechenden Input
        cO.Output([
                      "Bitte gib die Wachszeit der Kornart an, die du anlegen möchtest"]).printString()  # Welche Daten sind gebraucht
        self.grow_time = int(input("» "))  # Warten auf entsprechenden Input
        cO.Output([
                      "Bitte gib den Kornabstand der Kornart an, die du anlegen möchtest"]).printString()  # Welche Daten sind gebraucht
        self.seed_space = int(input("» "))  # Warten auf entsprechenden Input
        cO.Output([
                      "Bitte gib den Reihenabstand der Kornart an, die du anlegen möchtest"]).printString()  # Welche Daten sind gebraucht
        self.row_space = int(input("» "))  # Warten auf entsprechenden Input
        return self.name, self.grow_time, self.seed_space, self.row_space  # zurückgeben der gesammelten Daten

    def fieldData(self):
        cO.Output(["Bitte gib die Länge des Feldes in km ein"]).printString()  # Welche Daten sind gebraucht
        self.height = int(input("» "))  # Warten auf entsprechenden Input
        cO.Output(["Bitte gib die Breite des Feldes in km ein"]).printString()  # Welche Daten sind gebraucht
        self.width = int(input("» "))  # Warten auf entsprechenden Input
        return self.height, self.width  # zurückgeben der gesammelten Daten

    def TractorData(self):
        cO.Output(["Bitte gib den Namen des Traktors ein"]).printString()  # Welche Daten sind gebraucht
        self.name = input("» ")  # Warten auf entsprechenden Input
        cO.Output(["Bitte den Spritverbrauch pro Stunde an"]).printString()  # Welche Daten sind gebraucht
        self.fuelUsage = input("» ")  # Warten auf entsprechenden Input
        cO.Output(["Bitte gib die Durchschnittsgeschwindigkeit an"]).printString()  # Welche Daten sind gebraucht
        self.avSpeed = input("» ")  # Warten auf entsprechenden Input
        return self.name, self.fuelUsage, self.avSpeed  # zurückgeben der gesammelten Daten

    def Fields(self):
        self.result = main.connection.qry_stmt("SELECT * FROM fields")  # Daten zu Feldern von Datenbank erhalten
        return self.result  # zurückgeben der gesammelten Daten

    def Saat(self):
        self.result = main.connection.qry_stmt("SELECT * FROM saat")  # Daten zur Saat von Datenbank erhalten
        return self.result  # zurückgeben der gesammelten Daten

    def Tractor(self):
        self.result = main.connection.qry_stmt("SELECT * FROM tractors")  # Daten zu Traktoren von Datenbank erhalten
        return self.result  # zurückgeben der gesammelten Daten

    def seeds(self, seed):
        # print(f"versuche Daten für {seed} zu erhalten")
        self.result = main.connection.qry_stmt("SELECT * FROM saat WHERE name = %s;", (seed,))
        self.result = str(self.result).replace("(", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace(")", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("'", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace(" ", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("[", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("]", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).split(",")  # Entfernen unnötiger Satzzeichen aus string
        # print(f"Erhaltene Daten: {self.result}")
        return self.result  # zurückgeben der gesammelten Daten

    def Field(self, nummer):
        # print(f"versuche Daten für Feld {nummer} zu erhalten")
        self.result = main.connection.qry_stmt("SELECT * FROM fields WHERE id = %s;", (nummer,))
        self.result = str(self.result).replace("(", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace(")", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("'", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace(" ", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("[", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("]", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).split(",")  # Entfernen unnötiger Satzzeichen aus string
        # print(f"Erhaltene Daten: {self.result}")
        return self.result  # zurückgeben der gesammelten Daten

    def Tractors(self, nummer):
        self.result = main.connection.qry_stmt("SELECT * FROM tractors WHERE id = %s;", (nummer,))
        self.result = str(self.result).replace("(", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace(")", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("'", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace(" ", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("[", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).replace("]", "")  # Entfernen unnötiger Satzzeichen aus string
        self.result = str(self.result).split(",")  # Entfernen unnötiger Satzzeichen aus string
        return self.result  # zurückgeben der gesammelten Daten
