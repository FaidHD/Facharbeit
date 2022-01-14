import database as db
import command as cmd

connection = db.Connection(
    hostname="db.faidhd.de",
    database="facharbeit",
    username="facharbeit",
    password="PhVS_-T0nNc7*K3]",
)


class Main:

    def __init__(self):
        self.connection = connection
        self.command_manager = None

    def start(self):
        self.connection.execute_stmt(
            "CREATE TABLE IF NOT EXISTS saat(`name` VARCHAR(255), `wachszeit` INTEGER NOT NULL, `kornabstand` INTEGER NOT NULL, `reihenabstand` INTEGER NULL, PRIMARY KEY(`name`));") # SQL Abfrage zur erstellung der benötigten Tabellen

        self.command_manager = cmd.CommandManager() # Initialisierung des CommandManagers
        self.command_manager.register_command(cmd.HelpCommand(self))                #
        self.command_manager.register_command(cmd.CreateSeedCommand())              #
        self.command_manager.register_command(cmd.CreateFieldCommand())             #
        self.command_manager.register_command(cmd.ShowSeedsCommand())               #   Registrierung der Commands
        self.command_manager.register_command(cmd.DeleteSeedCommand())              #
        self.command_manager.register_command(cmd.ShowFieldsCommand())              #
        self.command_manager.register_command(cmd.GrowCalculationCommand())         #
        self.command_manager.register_command(cmd.OpenMenuCommand(self))            #
        self.command_manager.wait_for_command_input() # Abfangen der Nutzereingaben starten


if __name__ == "__main__":
    main = Main()
    main.start()


def stop():
    connection.close()
    print("Shutting down...")
