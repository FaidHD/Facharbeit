import main


class CreateSeed:

    def __init__(self, name, wachszeit, kornabstand, reihenabstand):
        self.con = main.connection  # referenz zur Verbindung mit der Datenbank

        self.data = (name, wachszeit, kornabstand, reihenabstand)  # Daten werden in data Variable zusammengefasst
        self.stmt = "INSERT INTO `saat`(`name`, `wachszeit`, `kornabstand`, `reihenabstand`) VALUES (%s,%s,%s,%s)"  # Daten werden als SQL Statement formatiert
        self.save_data()  # Aufruf zur endgültigen abspeicherung

    def save_data(self):
        main.connection.execute_stmt(self.stmt, self.data)  # Endgültige abspeicherung
        return "New seed added to Database"


class CreateField:
    def __init__(self, height, width):
        self.con = main.connection  # referenz zur Verbindung mit der Datenbank

        self.data = (None, height, width, 0)  # Daten werden in data Variable zusammengefasst
        self.stmt = "INSERT INTO `fields`(`id`, `height`, `width`, `currentlyUsed`) VALUES (%s,%s,%s,%s)"  # Daten werden als SQL Statement formatiert
        self.save_data()  # Aufruf zur endgültigen abspeicherung

    def save_data(self):
        main.connection.execute_stmt(self.stmt, self.data)  # Endgültige abspeicherung
        return "New Field added to Database"


class CreateTractor:
    def __init__(self, name, fuelUsage, speed):
        self.con = main.connection  # referenz zur Verbindung mit der Datenbank

        self.data = (None, name, fuelUsage, speed)  # Daten werden in data Variable zusammengefasst
        self.stmt = "INSERT INTO `tractors`(`id`, `name`, `fuelUsage`, `speed`) VALUES (%s,%s,%s,%s)"  # Daten werden als SQL Statement formatiert
        self.save_data()  # Aufruf zur endgültigen abspeicherung

    def save_data(self):
        main.connection.execute_stmt(self.stmt, self.data)  # Endgültige abspeicherung
        return "New Tractor added to Database"
