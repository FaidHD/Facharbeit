import main


class GetData:

    def __init__(self):
        self.seed = ""
        self.name = ""
        self.grow_time = ""
        self.seed_space = ""
        self.row_space = ""
        self.result = []
        self.height = []
        self.width = []
        pass

    def seedData(self):
        print("Bitte gib den Namen der Kornart an, die du anlegen möchtest")
        self.name = input("» ")
        print("Bitte gib die Wachszeit der Kornart an, die du anlegen möchtest")
        self.grow_time = int(input("» "))
        print("Bitte gib den Kornabstand der Kornart an, die du anlegen möchtest")
        self.seed_space = int(input("» "))
        print("Bitte gib den Reihenabstand der Kornart an, die du anlegen möchtest")
        self.row_space = int(input("» "))
        return self.name, self.grow_time, self.seed_space, self.row_space

    def Fields(self):
        self.result = main.connection.qry_stmt("SELECT * FROM fields")
        return self.result

    def Saat(self):
        self.result = main.connection.qry_stmt("SELECT * FROM saat")
        return self.result
    
    def seeds(self, seed):
        print(f"versuche Daten für {seed} zu erhalten")
        self.result = main.connection.qry_stmt("SELECT * FROM saat WHERE name = %s;", (seed,))
        self.result = str(self.result).replace("(", "")
        self.result = str(self.result).replace(")", "")
        self.result = str(self.result).replace("'", "")
        self.result = str(self.result).replace(" ", "")
        self.result = str(self.result).replace("[", "")
        self.result = str(self.result).replace("]", "")
        self.result = str(self.result).split(",")
        print(f"Erhaltene Daten: {self.result}")
        return self.result

    def Field(self, nummer):
        print(f"versuche Daten für Feld {nummer} zu erhalten")
        self.result = main.connection.qry_stmt("SELECT * FROM fields WHERE id = %s;", (nummer,))
        self.result = str(self.result).replace("(", "")
        self.result = str(self.result).replace(")", "")
        self.result = str(self.result).replace("'", "")
        self.result = str(self.result).replace(" ", "")
        self.result = str(self.result).replace("[", "")
        self.result = str(self.result).replace("]", "")
        self.result = str(self.result).split(",")
        print(f"Erhaltene Daten: {self.result}")
        return self.result
