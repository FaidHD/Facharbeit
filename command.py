import saaterstellung as sad
import growCalculation as gC
import createOutput as cO
import main
import menu


class CommandManager:

    def __init__(self):
        self.registered_commands = []

    def register_command(self, command):
        self.registered_commands.append(command)

    def wait_for_command_input(self):
        gib_was_ein = input("» ")
        name = gib_was_ein.split(" ")[0]
        args = []
        if name != gib_was_ein:
            args = gib_was_ein.replace(name + " ", "").split(" ")
        if name.lower() == "stop" or name.lower() == "quit":
            main.stop()
            return

        for command in self.registered_commands:
            if command.name == name:
                command.call(args)
                self.wait_for_command_input()
                return
        print("Command nicht gefunden. Um eine Liste an Befehlen zu erhalten, nutze \"help\"")
        self.wait_for_command_input()

    def get_commands(self):
        return self.registered_commands


class Command:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def call(self, args):
        print("Call method from command" + self.name + " not defined")


class HelpCommand(Command):

    def __init__(self, main_instance):
        super().__init__("help", "Liste alle verfügbaren Befehle auf")
        self.main_instance = main_instance

    def call(self, args):
        print(f"stop - Beende das Programm")
        for command in self.main_instance.command_manager.get_commands():
            print(f"{command.name} - {command.description}")
            pass


class CreateSeedCommand(Command):

    def __init__(self):
        super().__init__("createSeed", "Füge eine neue Kornart in der Datenbank hinzu")

    def call(self, args):
        if len(args) == 4:
            try:
                name = args[0]
                wachszeit = int(args[1])
                kornabstand = int(args[2])
                reihenabstand = int(args[3])
                sad.Create(name, wachszeit, kornabstand, reihenabstand)
                print(f"Die Saat {name} wurde erfolgreich erstellt")
            except ValueError:
                print("Bitte benutze: createSeed <Name> <Wachszeit> <Kornabstand> <Reihenabstand>")
        else:
            print("Bitte benutze: createSeed <Name> <Wachszeit> <Kornabstand> <Reihenabstand>")


class ShowSeedsCommand(Command):

    def __init__(self):
        super().__init__("showSeeds", "Zeige alle verfügbaren Kornarten an")

    def call(self, args):
        if len(args) != 0:
            print("Bitte benutze: showSeeds")
            return
        result = main.connection.qry_stmt("SELECT * FROM saat")
        for r in result:
            print(r[0], r[1], r[2], r[3])


class DeleteSeedCommand(Command):

    def __init__(self):
        super().__init__("deleteSeed", "Lösche eine Kornart aus der Datenbank")

    def call(self, args):
        if len(args) != 1:
            print("Bitte benutze: deleteSeed <Name>")
            return
        if args[0] == "all":
            main.connection.execute_stmt("DELETE FROM saat")
            print("Alle Einträge gelöscht")
        else:
            main.connection.execute_stmt("DELETE FROM saat WHERE name= %s", (args[0],))
            print(f"{args[0]} wurde aus der Datenbank gelöscht.")


class ShowFieldsCommand(Command):
    def __init__(self):
        super().__init__("showFields", "Zeige alle verfügbaren Felder an")

    def call(self, args):
        if len(args) != 0:
            print("Bitte benutze: showFields")
            return
        result = main.connection.qry_stmt("SELECT * FROM fields")
        for r in result:
            print(r[0], r[1], r[2], r[3])


class GrowCalculation(Command):
    def __init__(self):
        super().__init__("growCalculation", "Führe Saat und Felder berechnung durch")

    def call(self, args):
        if len(args) != 2:
            print("Bitte benutze: growCalculation <FeldID> <SaatgutName>")
            return
        else:
            try:
                seedCount, xCount, yCount = gC.GrowCalculation(args[0], args[1]).calcCount()
                cO.Output([f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden"]).printString()
                cO.Output([f"Auf dieses Feld passen insgesamt {seedCount} der gewählen Saatart"]).printString()
            except:
                cO.Output(["Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut"]).printString()


class OpenMenu(Command):

    def __init__(self, main_instance):
        super().__init__("menu", "Öffne das Menu")
        self.main_instance = main_instance

    def call(self, args):
        if len(args) != 0:
            cO.Output("Bitte benutze: menu").printString()
            return

        menu.Menu(self.main_instance)
