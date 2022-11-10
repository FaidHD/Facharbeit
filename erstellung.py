import main


class CreateSeed:

    def __init__(self, name, wachszeit, kornabstand, reihenabstand):
        self.con = main.connection

        self.data = (name, wachszeit, kornabstand, reihenabstand)
        self.stmt = "INSERT INTO `saat`(`name`, `wachszeit`, `kornabstand`, `reihenabstand`) VALUES (%s,%s,%s,%s)"
        self.save_data()

    def save_data(self):
        main.connection.execute_stmt(self.stmt, self.data)
        return "New seed added to Database"


class CreateField:
    def __init__(self, height, width):
        self.con = main.connection

        self.data = (None, height, width, 0)
        self.stmt = "INSERT INTO `fields`(`id`, `height`, `width`, `currentlyUsed`) VALUES (%s,%s,%s,%s)"
        self.save_data()

    def save_data(self):
        main.connection.execute_stmt(self.stmt, self.data)
        return "New Field added to Database"


class CreateTractor:
    def __int__(self, name, fuelUsage, speed):
        self.con = main.connection

        self.data = (None, name, fuelUsage, speed)
        self.stmt = "INSERT INTO `tractors`(`id`, `name`, `fuelUsage`, `speed`) VALUES (%s,%s,%s,%s)"
        self.save_data()

    def save_date(self):
        main.connection.execute_stmt(self.stmt, self.data)
        return "New Tractor added to Database"
