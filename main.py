import database as db
import command as cmd
import saaterstellung as sad
import menu

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
            "CREATE TABLE IF NOT EXISTS saat(`name` VARCHAR(255), `wachszeit` INTEGER NOT NULL, `kornabstand` INTEGER NOT NULL, `reihenabstand` INTEGER NULL, PRIMARY KEY(`name`));")
        # menu.Menu()

        self.command_manager = cmd.CommandManager()
        self.command_manager.register_command(cmd.CreateSeedCommand())
        self.command_manager.register_command(cmd.ShowSeedsCommand())
        self.command_manager.register_command(cmd.DeleteSeedCommand())
        self.command_manager.wait_for_command_input()

    # def show_seeds(self):
    #     # Verbindung, Cursor
    #     connection = sqlite3.connect("Saatgut.db")
    #     cursor = connection.cursor()
    #
    #     # SQL-Abfrage
    #     sql = "SELECT * FROM saat"
    #
    #     cursor.execute(sql)
    #
    #     # Ausgabe des Ergebnisses
    #     for dsatz in cursor:
    #         print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    #
    #     # Verbindung beenden
    #     connection.close()
    #     print("Press Enter to continue!")
    #     input()
    #     self.start()


if __name__ == "__main__":
    main = Main()
    main.start()


def stop():
    connection.close()
    print("Shutting down...")
