import erstellung as sad
import main
import getData as gD
import growCalculation as gC
import createOutput as cO


class Menu:

    def __init__(self, main_instance):
        self.command = None
        self.menu(main_instance)

    def menu(self, main_instance):
        cO.Output(["1) Zeige die Liste der Verfügbaren Kornarten",
                   "2) Zeige die Líste der verfügbaren Felder",
                   "3) Füge eine neue Kornart hinzu",
                   "4) Füge ein neues Feld hinzu",
                   "5) Führe eine Feldberechnung durch",
                   "6) Beende dieses Menu",
                   "Bitte gib eine der Nummern ein: "]).printString()
        is_input_number = True
        while is_input_number:
            try:
                self.command = int(input("» "))
                is_input_number = False
            except ValueError:
                cO.Output(["Falsches Format! Bitte gib eine Zahl ein"]).printString()

        if self.command == 1:
            result = main.connection.qry_stmt("SELECT * FROM saat")
            strings = []
            for i in result:
                strings.append(f"Name: {i[0]} | Wachzeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
            strings.append("Drücke eine Taste um fortzufahren")
            cO.Output(strings).printString()
            input()
            self.menu(main_instance)

        elif self.command == 2:
            result = main.connection.qry_stmt("SELECT * FROM fields")
            strings = []
            for i in result:
                strings.append(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
            strings.append("Drücke eine Taste um fortzufahren")
            cO.Output(strings).printString()
            input()
            self.menu(main_instance)

        elif self.command == 3:
            data = gD.GetData().seedData()
            sad.CreateSeed(data[0], data[1], data[2], data[3])
            cO.Output([f"Das Saatgut {data[0]} wurde erfolgreich erstellt"]).printString()
            self.menu(main_instance)

        elif self.command == 4:
            data = gD.GetData().fieldData()
            sad.CreateField(data[0], data[1])
            cO.Output(["Das Feld wurde erfolgreich erstellt", "Drücke Enter um fortzufahren"]).printString()
            input()
            self.menu(main_instance)

        elif self.command == 5:

            strings = ["Bitte wähle eins dieser Felder und gib die entsprechende ID ein:", "-------------------------------------"]
            for i in gD.GetData().Fields():
                strings.append(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
            cO.Output(strings).printString()
            FieldID = int(input("» "))

            strings = ["Bitte wähle eins der Saatgüter und gib den Namen ein:", "-------------------------------------"]
            for i in gD.GetData().Saat():
                strings.append(f"Name: {i[0]} | Wachzeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
            cO.Output(strings).printString()
            SeedName = input("» ")

            try:
                seedCount, xCount, yCount = gC.GrowCalculation(FieldID, SeedName).calcCount()
                cO.Output([f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden", f"Auf dieses Feld passen insgesamt {seedCount} der gewählen Saatart", "Drücke eine Taste um fortzufahren"]).printString()
                input()
            except:
                cO.Output(["Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut", "Drücke eine Taste um fortzufahren"]).printString()
                input()

            self.menu(main_instance)

        elif self.command == 6:
            cO.Output(["Menu verlassen. Gib einen Befehl ein"]).printString()
        else:
            cO.Output(["please Enter a Valid Number. Press Enter to try again."]).printString()
            self.menu(main_instance)
