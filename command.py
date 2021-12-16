import erstellung as sad
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
        cO.Output(["Command nicht gefunden. Um eine Liste an Befehlen zu erhalten, nutze \"help\""]).printString()
        self.wait_for_command_input()

    def get_commands(self):
        return self.registered_commands


class Command:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def call(self, args):
        cO.Output(["Call method from command" + self.name + " not defined"]).printString()


class HelpCommand(Command):

    def __init__(self, main_instance):
        super().__init__("help", "Liste alle verfügbaren Befehle auf")
        self.main_instance = main_instance

    def call(self, args):
        cO.Output([f"stop - Beende das Programm"]).printString()
        strings = []
        for command in self.main_instance.command_manager.get_commands():
            strings.append(f"{command.name} - {command.description}")
        cO.Output(strings).printString()


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
                sad.CreateSeed(name, wachszeit, kornabstand, reihenabstand)
                cO.Output([f"Die Saat {name} wurde erfolgreich erstellt"]).printString()
            except ValueError:
                cO.Output(["Bitte benutze: createSeed <Name> <Wachszeit> <Kornabstand> <Reihenabstand>"]).printString()
        else:
            cO.Output(["Bitte benutze: createSeed <Name> <Wachszeit> <Kornabstand> <Reihenabstand>"]).printString()


class CreateFieldCommand(Command):
    def __init__(self):
        super().__init__("createField", "Erstelle ein neues Feld")

    def call(self, args):
        if len(args) != 2:
            cO.Output(["Bitte benutze createField <height> <width>"]).printString()
            return
        else:
            sad.CreateField(int(args[0]), int(args[1]))
            cO.Output(["Das Feld wurde erfolgreich erstellt"]).printString()


class ShowSeedsCommand(Command):

    def __init__(self):
        super().__init__("showSeeds", "Zeige alle verfügbaren Kornarten an")

    def call(self, args):
        if len(args) != 0:
            cO.Output(["Bitte benutze: showSeeds"]).printString()
            return
        result = main.connection.qry_stmt("SELECT * FROM saat")
        strings = []
        for i in result:
            strings.append(f"Name: {i[0]} | Wachszeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")
        cO.Output(strings).printString()


class DeleteSeedCommand(Command):

    def __init__(self):
        super().__init__("deleteSeed", "Lösche eine Kornart aus der Datenbank")

    def call(self, args):
        if len(args) != 1:
            cO.Output("Bitte benutze: deleteSeed <Name>").printString()
            return
        if args[0] == "all":
            main.connection.execute_stmt("DELETE FROM saat")
            cO.Output(["Alle Einträge gelöscht"]).printString()
        else:
            main.connection.execute_stmt("DELETE FROM saat WHERE name= %s", (args[0],))
            cO.Output([f"{args[0]} wurde aus der Datenbank gelöscht."]).printString()


class ShowFieldsCommand(Command):
    def __init__(self):
        super().__init__("showFields", "Zeige alle verfügbaren Felder an")

    def call(self, args):
        if len(args) != 0:
            cO.Output(["Bitte benutze: showFields"]).printString()
            return
        result = main.connection.qry_stmt("SELECT * FROM fields")
        strings = []
        for i in result:
            strings.append(f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")
        cO.Output(strings).printString()


class GrowCalculationCommand(Command):
    def __init__(self):
        super().__init__("growCalculation", "Führe Saat und Felder berechnung durch")

    def call(self, args):
        if len(args) != 2:
            cO.Output(["Bitte benutze: growCalculation <FeldID> <SaatgutName>"]).printString()
            return
        else:
            try:
                seedCount, xCount, yCount = gC.GrowCalculation(args[0], args[1]).calcCount()
                cO.Output([f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden", f"Auf dieses Feld passen insgesamt {seedCount} der gewählen Saatart"]).printString()
            except:
                cO.Output(["Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut"]).printString()


class OpenMenuCommand(Command):

    def __init__(self, main_instance):
        super().__init__("menu", "Öffne das Menu")
        self.main_instance = main_instance

    def call(self, args):
        if len(args) != 0:
            cO.Output(["Bitte benutze: menu"]).printString()
            return

        menu.Menu(self.main_instance)
