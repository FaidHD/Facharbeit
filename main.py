import database as db
import command as cmd

connection = db.Connection(
    hostname="38.242.241.136",
    database="facharbeit",
    username="facharbeit",
    password="PhVS_-T0nNc7*K3]",
)


class Main:

    def __init__(self):
        self.connection = connection
        self.command_manager = None

    def start(self):
        self.connection.execute_stmt("CREATE TABLE IF NOT EXISTS saat(`name` VARCHAR(255), `wachszeit` INT NOT NULL, `kornabstand` INT NOT NULL, `reihenabstand` INT NULL, PRIMARY KEY(`name`));")  # SQL Abfragen zur erstellung der benötigten Tabellen
        self.connection.execute_stmt("CREATE TABLE IF NOT EXISTS fields(`id` INT NOT NULL AUTO_INCREMENT, `height` INT DEFAULT NULL, `width` INT DEFAULT NULL, `currentlyUsed` TINYINT DEFAULT NULL, PRIMARY KEY(`id`));")  # SQL Abfragen zur erstellung der benötigten Tabellen
        self.connection.execute_stmt("CREATE TABLE IF NOT EXISTS tractors(`id` INT NOT NULL AUTO_INCREMENT, `name` TINYTEXT NOT NULL DEFAULT 'name missing', `fuelUsage` INT NOT NULL DEFAULT 0, `speed` INT NULL DEFAULT 0, PRIMARY KEY(`id`), UNIQUE KEY `name` (`name`));")  # SQL Abfragen zur erstellung der benötigten Tabellen
        self.connection.execute_stmt("CREATE TABLE IF NOT EXISTS `growing` (`id` int(11) NOT NULL AUTO_INCREMENT, `field` int(11) NOT NULL, `saat` varchar(255) NOT NULL, `time_seeded` timestamp NOT NULL DEFAULT NOW(), PRIMARY KEY (`id`), KEY `field` (`field`), KEY `saat` (`saat`), CONSTRAINT `field` FOREIGN KEY (`field`) REFERENCES `fields` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `saat` FOREIGN KEY (`saat`) REFERENCES `saat` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION );")  # SQL Abfragen zur erstellung der benötigten Tabellen

        self.command_manager = cmd.CommandManager()  # Initialisierung des CommandManagers
        menu_command = cmd.OpenMenuCommand(self)
        self.command_manager.register_command(cmd.HelpCommand(self))  #
        self.command_manager.register_command(cmd.CreateSeedCommand())  #
        self.command_manager.register_command(cmd.CreateFieldCommand())  #
        self.command_manager.register_command(cmd.CreateTractorCommand()) #
        self.command_manager.register_command(cmd.ShowSeedsCommand())  # Registrierung der Commands
        self.command_manager.register_command(cmd.DeleteSeedCommand())  #
        self.command_manager.register_command(cmd.ShowFieldsCommand())  #
        self.command_manager.register_command(cmd.GrowCalculationCommand())  #
        self.command_manager.register_command(menu_command)  #
        menu_command.call([])  # Abfangen der Nutzereingaben starten


if __name__ == "__main__":
    main = Main()
    main.start()


def stop():
    connection.close()
    print("Shutting down...")
