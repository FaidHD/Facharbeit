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
        print("3) Beende dieses Menu")
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
            print("")
            print("Menu verlassen. Gib einen Befehl ein")
        else:
            print("please Enter a Valid Number. Press Enter to try again.")
            self.menu(main_instance)
