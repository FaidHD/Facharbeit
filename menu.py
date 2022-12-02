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
                   "2) Zeige die Liste der verfügbaren Felder",
                   "3) Zeige die Liste der verfügbaren Traktoren",
                   "4) Füge eine neue Kornart hinzu",
                   "5) Füge ein neues Feld hinzu",
                   "6) Füge einen neuen Traktor hinzu",
                   "7) Führe eine Feldberechnung durch",
                   "8) Beenden",
                   "Bitte gib eine der Nummern ein: "]).printString()  # Output der verfügbaren Optionen
        is_input_number = True
        while is_input_number:
            try:
                self.command = int(input("» "))  # warten auf Eingabe
                is_input_number = False
            except ValueError:
                cO.Output([
                    "Falsches Format! Bitte gib eine Zahl ein"]).printString()  # Wenn keine Zahl eingegeben wird Error ausgegeben

        if self.command == 1:  # Wenn Command gleich 1
            result = main.connection.qry_stmt("SELECT * FROM saat")  # Alle Daten zur Saat von der Datenbank erhalten
            strings = []
            for i in result:  # Für jede Saatart wird ein String mit dessen Daten ausgegeben
                strings.append(f"Name: {i[0]} | Wachzeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
            strings.append("Drücke eine Taste um fortzufahren")
            cO.Output(strings).printString()  # Wird an unsere Custom Printfunktion übergeben
            input()  # warten auf Tastendruck um fortzufahren
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 2:
            result = main.connection.qry_stmt(
                "SELECT * FROM fields")  # Alle Daten zu den Feldern von der Datenbank erhalten
            strings = []
            for i in result:  # Für jedes Feld wird ein String mit dessen Daten ausgegeben
                strings.append(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
            strings.append("Drücke eine Taste um fortzufahren")
            cO.Output(strings).printString()  # Wird an unsere Custom Printfunktion übergeben
            input()  # warten auf Tastendruck um fortzufahren
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 3:
            result = main.connection.qry_stmt(
                "SELECT * FROM tractors")  # Alle Daten zu Traktoren von der Datenbank erhalten
            strings = []
            for i in result:  # Für jeden Traktor wird ein String mit dessen Daten ausgegeben
                strings.append(f"Name: {i[1]} | Verbrauch: {i[2]}L/h | Durchschnittsgeschwindigkeit: {i[3]}km/h")
            strings.append("Drücke eine Taste um fortzufahren")
            cO.Output(strings).printString()  # Wird an unsere Custom Printfunktion übergeben
            input()  # warten auf Tastendruck um fortzufahren
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 4:
            data = gD.GetData().seedData()  # Daten werden durch die GetData Funktion gesammelt
            sad.CreateSeed(data[0], data[1], data[2], data[3])  # Saatgut wird erstellt
            cO.Output([f"Das Saatgut {data[0]} wurde erfolgreich erstellt",
                       "Drücke Enter um fortzufahren"]).printString()  # Wird an unsere Custom Printfunktion übergeben
            input()  # warten auf Tastendruck um fortzufahren
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 5:
            data = gD.GetData().fieldData()  # Daten werden durch die GetData Funktion gesammelt
            sad.CreateField(data[0], data[1])  # Saatgut wird erstellt
            cO.Output(["Das Feld wurde erfolgreich erstellt",
                       "Drücke Enter um fortzufahren"]).printString()  # Wird an unsere Custom Printfunktion übergeben
            input()  # warten auf Tastendruck um fortzufahren
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 6:
            data = gD.GetData().TractorData()  # Daten werden durch die GetData Funktion gesammelt
            sad.CreateTractor(data[0], data[1], data[2])  # Saatgut wird erstellt
            cO.Output([f"Der Traktor {data[0]} wurde erfolgreich erstellt",
                       "Drücke Enter um fortzufahren"]).printString()  # Wird an unsere Custom Printfunktion übergeben
            input()  # warten auf Tastendruck um fortzufahren
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 7:
            try:
                strings = ["Bitte wähle eins dieser Felder und gib die entsprechende ID ein:",
                           "-------------------------------------"]
                for i in gD.GetData().Fields():  # verfügbare Felder werden zur Auswahl angezeigt
                    strings.append(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
                cO.Output(strings).printString()  # Wird an unsere Custom Printfunktion übergeben
                FieldID = int(input("» "))  # Warten auf Input einer Felder-ID
            except:
                print(
                    "Etwas ist schiefgelaufen! Drücke Enter um ins Hauptmenü zurück zu gelangen")  # Falls ein Formatfehler vorliegt, wird ein Error ausgegeben
                input()  # warten auf Tastendruck um fortzufahren
                self.menu(main_instance)  # Menu ruft sich wieder selbst auf

            try:
                strings = ["Bitte wähle eins der Saatgüter und gib den Namen ein:",
                           "-------------------------------------"]
                for i in gD.GetData().Saat():  # verfügbare Saatarten werden zur Auswahl angezeigt
                    strings.append(f"Name: {i[0]} | Wachzeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
                cO.Output(strings).printString()  # Wird an unsere Custom Printfunktion übergeben
                SeedName = input("» ")  # Warten auf Input eines Saatgutnamens
            except:
                print(
                    "Etwas ist schiefgelaufen! Drücke Enter um ins Hauptmenü zurück zu gelangen")  # Falls ein Formatfehler vorliegt, wird ein Error ausgegeben
                input()  # warten auf Tastendruck um fortzufahren
                self.menu(main_instance)  # Menu ruft sich wieder selbst auf

            try:
                strings = ["Bitte wähle einen der traktoren und gib die ID ein:",
                           "-------------------------------------"]
                for i in gD.GetData().Tractor():  # verfügbare traktoren werden zur Auswahl angezeigt
                    strings.append(
                        f"ID: {i[0]} | Name: {i[1]} | Verbrauch: {i[2]}L/h | Durchschnittsgeschwindigkeit: {i[3]}km/h")
                cO.Output(strings).printString()  # Wird an unsere Custom Printfunktion übergeben
                TractorID = int(input("» "))  # Warten auf Input einer Traktor-ID

            except:
                print(
                    "Etwas ist schiefgelaufen! Drücke Enter um ins Hauptmenü zurück zu gelangen")  # Falls ein Formatfehler vorliegt, wird ein Error ausgegeben
                input()  # warten auf Tastendruck um fortzufahren
                self.menu(main_instance)  # Menu ruft sich wieder selbst auf

            try:
                seedCount, xCount, yCount, milageDriven, timeDriven, fuelUsed, fuelCost = gC.GrowCalculation(FieldID,
                                                                                                             SeedName,
                                                                                                             TractorID).calcData()  # anforderungen aller berechneten Daten von GrowCalculation
                cO.Output([f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden",
                           f"Auf dieses Feld passen insgesamt {seedCount} der gewählten Saatart",
                           f"Mit diesem Traktor wird eine Distanz von {milageDriven / 100}km zurückgelegt. Diese Distanz wird in {timeDriven}h gefahren und wird {fuelUsed}L verbrauchen, was bei einem Preis von 1.89€ {fuelCost}€ kosten wird",
                           "Drücke eine Taste um fortzufahren"]).printString()  # Wird an unsere Custom Printfunktion übergeben
                input()  # warten auf Tastendruck um fortzufahren
            except:
                cO.Output(["Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut",
                           "Drücke eine Taste um fortzufahren"]).printString()  # Falls ein Formatfehler vorliegt, wird ein Error ausgegeben
                input()  # warten auf Tastendruck um fortzufahren

            self.menu(main_instance)  # Menu ruft sich wieder selbst auf

        elif self.command == 8:
            cO.Output(
                ["Menu verlassen. Gib einen Befehl ein"]).printString()  # Wird an unsere Custom Printfunktion übergeben
            self.main_instance.command_manager.wait_for_command_input()
        else:
            cO.Output([
                "please Enter a Valid Number. Press Enter to try again."]).printString()  # Wird an unsere Custom Printfunktion übergeben
            self.menu(main_instance)  # Menu ruft sich wieder selbst auf
