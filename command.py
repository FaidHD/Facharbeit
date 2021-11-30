import saaterstellung as sad
import main
import menu


class CommandManager:

    def __init__(self):
        self.registered_commands = []

    def register_command(self, command):
        self.registered_commands.append(command)

    def wait_for_command_input(self):
        gib_was_ein = input("Bitte gib einen command ein ")
        name = gib_was_ein.split(" ")[0]
        args = []
        if name != gib_was_ein:
            args = gib_was_ein.replace(name + " ", "").split(" ")
        if name.lower() == "stop":
            main.stop()
            return
        for command in self.registered_commands:
            if command.name == name:
                command.call(args)
                break
        self.wait_for_command_input()


class Command:

    def __init__(self, name):
        self.name = name

    def call(self, args):
        print("Call method from command" + self.name + " not defined")


class CreateSeedCommand(Command):

    def __init__(self):
        super().__init__("createSeed")

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
        super().__init__("showSeeds")

    def call(self, args):
        if len(args) != 0:
            print("Bitte benutze: showSeeds")
            return
        result = main.connection.qry_stmt("SELECT * FROM saat")
        for r in result:
            print(r[0], r[1], r[2], r[3])


class DeleteSeedCommand(Command):

    def __init__(self):
        super().__init__("deleteSeed")

    def call(self, args):
        if len(args) != 1:
            print("Bitte benutze: deleteSeed <Name>")
            return
        main.connection.execute_stmt("DELETE FROM saat WHERE name= %s", (args[0],))
        print(f"{args[0]} wurde aus der Datenbank gelöscht.")


class OpenMenu(Command):

    def __init__(self):
        super().__init__("menu")

    def call(self, args):
        if len(args) != 0:
            print("Bitte benutze: menu")
            return

        menu.Menu()
