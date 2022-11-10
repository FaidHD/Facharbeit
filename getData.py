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
        cO.Output(["Bitte gib den Namen der Kornart an, die du anlegen möchtest"]).printString()
        self.name = input("» ")
        cO.Output(["Bitte gib die Wachszeit der Kornart an, die du anlegen möchtest"]).printString()
        self.grow_time = int(input("» "))
        cO.Output(["Bitte gib den Kornabstand der Kornart an, die du anlegen möchtest"]).printString()
        self.seed_space = int(input("» "))
        cO.Output(["Bitte gib den Reihenabstand der Kornart an, die du anlegen möchtest"]).printString()
        self.row_space = int(input("» "))
        return self.name, self.grow_time, self.seed_space, self.row_space

    def fieldData(self):
        cO.Output(["Bitte gib die höhe des Feldes ein"]).printString()
        self.height = int(input("» "))
        cO.Output(["Bitte gib die Breite des Feldes ein"]).printString()
        self.width = int(input("» "))
        return self.height, self.width

    def TractorData(self):
        cO.Output(["Bitte gib den Namen des Traktors ein"]).printString()
        self.name = input("» ")
        cO.Output(["Bitte den Spritverbrauch pro Stunde an"]).printString()
        self.fuelUsage = input("» ")
        cO.Output(["Bitte gib die Durchschnittsgeschwindigkeit an"]).printString()
        self.avSpeed = input("» ")
        return self.name, self.fuelUsage, self.avSpeed

    def Fields(self):
        self.result = main.connection.qry_stmt("SELECT * FROM fields")
        return self.result

    def Saat(self):
        self.result = main.connection.qry_stmt("SELECT * FROM saat")
        return self.result
    
    def seeds(self, seed):
        #print(f"versuche Daten für {seed} zu erhalten")
        self.result = main.connection.qry_stmt("SELECT * FROM saat WHERE name = %s;", (seed,))
        self.result = str(self.result).replace("(", "")
        self.result = str(self.result).replace(")", "")
        self.result = str(self.result).replace("'", "")
        self.result = str(self.result).replace(" ", "")
        self.result = str(self.result).replace("[", "")
        self.result = str(self.result).replace("]", "")
        self.result = str(self.result).split(",")
        #print(f"Erhaltene Daten: {self.result}")
        return self.result

    def Field(self, nummer):
        #print(f"versuche Daten für Feld {nummer} zu erhalten")
        self.result = main.connection.qry_stmt("SELECT * FROM fields WHERE id = %s;", (nummer,))
        self.result = str(self.result).replace("(", "")
        self.result = str(self.result).replace(")", "")
        self.result = str(self.result).replace("'", "")
        self.result = str(self.result).replace(" ", "")
        self.result = str(self.result).replace("[", "")
        self.result = str(self.result).replace("]", "")
        self.result = str(self.result).split(",")
        #print(f"Erhaltene Daten: {self.result}")
        return self.result
