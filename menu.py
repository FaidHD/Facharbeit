import saaterstellung as sad
import main
import getData as gD


class Menu:

    def __init__(self, main_instance):
        self.command = None
        self.menu(main_instance)

    def menu(self, main_instance):
        print("")
        print("1) Zeige die Liste der Verfügbaren Kornarten ")
        print("2) Füge eine neue Kornart hinzu")
        print("3) Führe eine Feldberechnung durch")
        print("4) Beende dieses Menu")
        print("Bitte gib eine der Nummern ein: ")
        is_input_number = True
        while is_input_number:
            try:
                self.command = int(input("» "))
                is_input_number = False
            except ValueError:
                print("Falsches Format! Bitte gib 1, 2 oder 3 ein")

        if self.command == 1:
            result = main.connection.qry_stmt("SELECT * FROM saat")
            for r in result:
                print(r[0], r[1], r[2], r[3])
            self.menu(main_instance)
        elif self.command == 2:
            data = gD.GetData().seedData()
            sad.Create(data[0], data[1], data[2], data[3])
            print(f"Das Saatgut {data[0]} wurde erfolgreich erstellt")
            self.menu(main_instance)

        elif self.command == 3:

            print("Bitte wähle eins dieser Felder und gib die entsprechende ID ein:")
            print("-------------------------------------")
            for i in gD.GetData().Fields():
                print(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
            print("-------------------------------------")
            FieldID = int(input("» "))

            print("Bitte wähle eins der Saatgüter und gib den Namen ein:")
            print("-------------------------------------")
            for i in gD.GetData().Saat():
                print(f"Name: {i[0]} | Wachzeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
            print("-------------------------------------")
            SeedName = input("» ")

            try:
                seedCount, xCount, yCount = gC.GrowCalculation(FieldID, SeedName).calcCount()
                print(f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden")
                print(f"Auf dieses Feld passen insgesamt {seedCount} der gewählen Saatart")
            except:
                print("Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut")


            self.menu(main_instance)
        elif self.command == 4:
            print("")
            print("Menu verlassen. Gib einen Befehl ein")
        else:
            print("please Enter a Valid Number. Press Enter to try again.")
            self.menu(main_instance)
