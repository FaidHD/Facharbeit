import erstellung as sad
import growCalculation as gC
import createOutput as cO
import main
import menu


class CommandManager:  # CommandManager Objekt - Es besteht nur eine Instanz dieses Objekts gleichzeitig im Programm

    def __init__(self):
        self.registered_commands = []  # Initialisierung der Liste, in der die Commands gespeichert werden

    def register_command(self, command):
        self.registered_commands.append(command)  # Hinzufügen eines Befehls in die Liste

    def wait_for_command_input(self):  # Verwaltung der Nutzereingaben außerhalb des Menüs
        gib_was_ein = input("» ")
        name = gib_was_ein.split(" ")[0]  # Separierung des Command-Namen aus der Nutzereingabe
        args = []  # Liste der Argumente, die an den Command weitergegeben wird
        if name != gib_was_ein:
            args = gib_was_ein.replace(name + " ", "").split(" ")  # Überschreibung der Liste mit den Usereingaben
        if name.lower() == "stop" or name.lower() == "quit":  # Abfrage, ob Eingabe, um das Programm zu beenden, ausgeführt wurde. Aus Sicherheitsgründen hier eingebaut
            main.stop()
            return

        for command in self.registered_commands:  # Durchgehen durch alle registrierten Befehle
            if command.name == name:
                command.call(args)  # Ausführen des Codes, der für diesen Befehl erstellt wurde
                self.wait_for_command_input()  # Erneute Ausführung dieser Methode
                return
        cO.Output([
                      "Command nicht gefunden. Um eine Liste an Befehlen zu erhalten, nutze \"help\""]).printString()  # Falls kein Befehl gefunden wurde
        self.wait_for_command_input()  # Erneute Ausführung dieser Methode

    def get_commands(self):
        return self.registered_commands  # Rückgabe der Command-Liste


class Command:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def call(self, args):
        cO.Output([
                      "Call method from command" + self.name + " not defined"]).printString()  # Falls die call Methode nicht überschrieben wird


class HelpCommand(Command):

    def __init__(self, main_instance):
        super().__init__("help",
                         "Liste alle verfügbaren Befehle auf")  # Initialisierung des übergeordneten Command Objekts
        self.main_instance = main_instance  # Um in der call Methode darauf zugreifen zu können

    def call(self, args):
        strings = [f"stop - Beende das Programm"]  # Initialisierung der Liste, die später ausgegeben wird
        for command in self.main_instance.command_manager.get_commands():  # Durch alle registrierten Befehle iterieren
            strings.append(
                f"{command.name} - {command.description}")  # Befehl als String in die Nutzerausgabe hinzufügen
        cO.Output(strings).printString()  # Liste ausgeben


class CreateSeedCommand(Command):

    def __init__(self):
        super().__init__("createSeed", "Füge eine neue Kornart in der Datenbank hinzu")

    def call(self, args):
        if len(args) == 4:  # Überprüfung der Anzahl der Argumente, da exakt 4 für diesen Command benötigt werden
            try:  # Da hier Strings zu Integern gemacht werden müssen
                name = args[0]
                wachszeit = int(args[1])
                kornabstand = int(args[2])
                reihenabstand = int(args[3])
                sad.CreateSeed(name, wachszeit, kornabstand,
                               reihenabstand)  # Übergabe der Argumente zur finalen Erstellung
                cO.Output([f"Die Saat {name} wurde erfolgreich erstellt"]).printString()  # Ausgabe für den Nutzer
            except ValueError:
                cO.Output([
                              "Bitte benutze: createSeed <Name> <Wachszeit> <Kornabstand> <Reihenabstand>"]).printString()  # Falls die Argumente nicht richtig verarbeitet werden konnten
        else:
            cO.Output([
                          "Bitte benutze: createSeed <Name> <Wachszeit> <Kornabstand> <Reihenabstand>"]).printString()  # Falls die Anzahl der Argumente nicht 4 entspricht


class CreateFieldCommand(Command):
    def __init__(self):
        super().__init__("createField", "Erstelle ein neues Feld")

    def call(self, args):
        if len(args) != 2:  # Überprüfung der Anzahl der Argumente, da exakt 2 für diesen Command benötigt werden
            cO.Output([
                          "Bitte benutze createField <height> <width>"]).printString()  # Falls die Anzahl der Argumente nicht 2 entspricht
            return
        else:
            sad.CreateField(int(args[0]), int(args[1]))  # Übergabe der Argumente zur finalen Erstellung
            cO.Output(["Das Feld wurde erfolgreich erstellt"]).printString()  # Ausgabe für den Nutzer


class CreateTractorCommand(Command):
    def __init__(self):
        super().__init__("createTractor", "Erstelle einen neuen Traktor")

    def call(self, args):
        if len(args) != 3:  # Überprüfung der Anzahl der Argumente, da exakt 2 für diesen Command benötigt werden
            cO.Output([
                          "Bitte benutze createTractor <name> <fuelUsage> <avSpeed>"]).printString()  # Falls die Anzahl der Argumente nicht 2 entspricht
            return
        else:
            sad.CreateTractor(args[0], int(args[1]), int(args[2]))  # Übergabe der Argumente zur finalen Erstellung
            cO.Output(["Das Traktor wurde erfolgreich erstellt"]).printString()  # Ausgabe für den Nutzer


class ShowSeedsCommand(Command):

    def __init__(self):
        super().__init__("showSeeds", "Zeige alle verfügbaren Kornarten an")

    def call(self, args):
        if len(args) != 0:  # Keine Argumente gefordert
            cO.Output(["Bitte benutze: showSeeds"]).printString()
            return
        result = main.connection.qry_stmt("SELECT * FROM saat")  # Weitergabe der SQL Abfrage an die Connection Instanz
        strings = []  # Erstellung der Liste für die Ausgabe
        for i in result:  # Durch die Ergebnisse der Datenbank iterieren
            strings.append(
                f"Name: {i[0]} | Wachszeit: {i[1]} | Kornabstand: {i[2]} | Reihenabstand: {i[3]}")  # Hinzufügen der einzelnen Teile in die Ausgabe-Liste
        cO.Output(strings).printString()  # Ausgabe der Liste


class DeleteSeedCommand(Command):

    def __init__(self):
        super().__init__("deleteSeed", "Lösche eine Kornart aus der Datenbank")

    def call(self, args):
        if len(args) != 1:  # Ein Argument gefordert
            cO.Output("Bitte benutze: deleteSeed <Name>").printString()
            return
        if args[0] == "all":  # Falls alle Saatgutarten gelöscht werden sollen
            main.connection.execute_stmt("DELETE FROM saat")  # Ausführung des SQL Befehls
            cO.Output(["Alle Einträge gelöscht"]).printString()  # Ausgabe für den Nutzer
        else:  # Falls nicht alle Saatgutarten gelöscht werden sollen
            main.connection.execute_stmt("DELETE FROM saat WHERE name= %s", (args[0],))  # Ausführung des SQL Befehls
            cO.Output([f"{args[0]} wurde aus der Datenbank gelöscht."]).printString()  # Ausgabe für den Nutzer


class ShowFieldsCommand(Command):
    def __init__(self):
        super().__init__("showFields", "Zeige alle verfügbaren Felder an")

    def call(self, args):
        if len(args) != 0:  # Keine Argumente gefordert
            cO.Output(["Bitte benutze: showFields"]).printString()
            return
        result = main.connection.qry_stmt("SELECT * FROM fields")  # Ausführung der SQL Abfrage
        strings = []  # Erstellung der Liste für die Ausgabe
        for i in result:  # Durch die Ergebnisse der Datenbank iterieren
            strings.append(
                f"Id: {i[0]} | Breite: {i[2]} | Höhe: {i[1]}")  # Hinzufügen der einzelnen Teile in die Ausgabe-Liste
        cO.Output(strings).printString()  # Ausgabe der Liste


class GrowCalculationCommand(Command):
    def __init__(self):
        super().__init__("growCalculation", "Führe Saat und Felder berechnung durch")

    def call(self, args):
        if len(args) != 3:  # Zwei Argumente gefordert
            cO.Output(["Bitte benutze: growCalculation <FeldID> <SaatgutName> <TraktorID>"]).printString()
            return
        else:
            try:
                seedCount, xCount, yCount, milageDriven, timeDriven, fuelUsed, fuelCost = gC.GrowCalculation(int(args[0]), args[1], int(args[2])).calcData()
                cO.Output([f"Es können {xCount} Reihen mit jeweils {yCount} Pflanzen gesät werden",
                           f"Auf dieses Feld passen insgesamt {seedCount} der gewählen Saatart",
                           f"Mit diesem Traktor wird eine Distanz von {milageDriven / 100}km zurückgelegt. Diese Distanz wird in {timeDriven}h gefahren und wird {fuelUsed}L verbrauchen, was bei einem Preis von 1.89€ {fuelCost}€ kosten wird"])\
                    .printString()
            except:
                cO.Output(["Berechnung Fehlgeschlagen, bitte versuchen Sie es erneut"]).printString()


class OpenMenuCommand(Command):  # Command, um in das Menu zu kommen (vereinfachter Eingabemodus)

    def __init__(self, main_instance):
        super().__init__("menu", "Öffne das Menu")
        self.main_instance = main_instance

    def call(self, args):
        if len(args) != 0:  # Keine Argumente gefordert
            cO.Output(["Bitte benutze: menu"]).printString()
            return

        menu.Menu(self.main_instance)  # Öffnen des Menüs
