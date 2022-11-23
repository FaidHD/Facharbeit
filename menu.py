import erstellung as sad
import main
import getData as gD
import growCalculation as gC
import createOutput as cO


class Menu:

    def __init__(self, main_instance):
        self.main_instance = main_instance
        self.command = None
        self.menu(main_instance)

    def menu(self, main_instance):
        cO.Output(["1) Zeige die Liste der Verfügbaren Kornarten",
                   "2) Zeige die Líste der verfügbaren Felder",
                   "3) Zeige die Liste der verfügbaren Traktoren",
                   "4) Füge eine neue Kornart hinzu",
                   "5) Füge ein neues Feld hinzu",
                   "6) Füge einen neuen Traktor hinzu",
                   "7) Führe eine Feldberechnung durch",
                   "8) Beenden",
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
            result = main.connection.qry_stmt("SELECT * FROM tractors")
            strings = []
            for i in result:
                strings.append(f"Name: {i[1]} | Verbrauch: {i[2]}L/h | Durchschnittsgeschwindigkeit: {i[3]}km/h")
            strings.append("Drücke eine Taste um fortzufahren")
            cO.Output(strings).printString()
            input()
            self.menu(main_instance)

        elif self.command == 4:
            data = gD.GetData().seedData()
            sad.CreateSeed(data[0], data[1], data[2], data[3])
            cO.Output([f"Das Saatgut {data[0]} wurde erfolgreich erstellt", "Drücke Enter um fortzufahren"]).printString()
            input()
            self.menu(main_instance)

        elif self.command == 5:
            data = gD.GetData().fieldData()
            sad.CreateField(data[0], data[1])
            cO.Output(["Das Feld wurde erfolgreich erstellt", "Drücke Enter um fortzufahren"]).printString()
            input()
            self.menu(main_instance)

        elif self.command == 6:
            data = gD.GetData().TractorData()
            print(data)
            sad.CreateTractor(data[0], data[1], data[2])
            cO.Output([f"Der Traktor {data[0]} wurde erfolgreich erstellt", "Drücke Enter um fortzufahren"]).printString()
            input()
            self.menu(main_instance)

        elif self.command == 7:
            try:
                strings = ["Bitte wähle eins dieser Felder und gib die entsprechende ID ein:", "-------------------------------------"]
                for i in gD.GetData().Fields():
                    strings.append(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
                cO.Output(strings).printString()
                FieldID = int(input("» "))
            except:
                print("Etwas ist schiefgelaufen! Drücke Enter um ins Hauptmenü zurück zu gelangen")
                input()
                self.menu(main_instance)

            try:
                strings = ["Bitte wähle eins der Saatgüter und gib den Namen ein:", "-------------------------------------"]
                for i in gD.GetData().Saat():
                    strings.append(f"Name: {i[0]} | Wachzeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
                cO.Output(strings).printString()
                SeedName = input("» ")
            except:
                print("Etwas ist schiefgelaufen! Drücke Enter um ins Hauptmenü zurück zu gelangen")
                input()
                self.menu(main_instance)

            try:
                strings = ["Bitte wähle einen der traktoren und gib die ID ein:", "-------------------------------------"]
                for i in gD.GetData().Tractor():
                    strings.append(f"ID: {i[0]} | Name: {i[1]} | Verbrauch: {i[2]}L/h | Durchschnittsgeschwindigkeit: {i[3]}km/h")
                cO.Output(strings).printString()
                TractorID = int(input("» "))

            except:
                print("Etwas ist schiefgelaufen! Drücke Enter um ins Hauptmenü zurück zu gelangen")
                input()
                self.menu(main_instance)

            try:
                seedCount, xCount, yCount, milageDriven, timeDriven, fuelUsed, fuelCost = gC.GrowCalculation(FieldID, SeedName, TractorID).calcData()
                cO.Output([f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden", f"Auf dieses Feld passen insgesamt {seedCount} der gewählen Saatart",
                           f"Mit diesem Traktor wird eine Distanz von {milageDriven/100}km zurückgelegt. Diese Distanz wird in {timeDriven}h gefahren und wird {fuelUsed}L verbrauchen, was bei einem Preis von 1.89€ {fuelCost}€ kosten wird",
                           "Drücke eine Taste um fortzufahren"]).printString()
                input()
            except:
                cO.Output(["Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut", "Drücke eine Taste um fortzufahren"]).printString()
                input()

            self.menu(main_instance)

        elif self.command == 8:
            cO.Output(["Menu verlassen. Gib einen Befehl ein"]).printString()
            self.main_instance.command_manager.wait_for_command_input()
        else:
            cO.Output(["please Enter a Valid Number. Press Enter to try again."]).printString()
            self.menu(main_instance)
