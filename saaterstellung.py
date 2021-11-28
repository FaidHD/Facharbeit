import main


class create:

    def __init__(self):
        self.con = main.connection

        self.name = input("Name: ")
        self.wachszeit = input("Wachszeit: ")
        self.kornabstand = input("Kornabstand: ")
        self.reihenabstand = input("Reihenabstand: ")
        print(self.name, self.wachszeit, self.kornabstand, self.reihenabstand)
        self.data = (self.name, self.wachszeit, self.kornabstand, self.reihenabstand)
        self.stmt = ("INSERT INTO `saat`(`name`, `wachszeit`, `kornabstand`, `reihenabstand`) VALUES (%s,%s,%s,%s)")
        self.save_data()

    def save_data(self):
        print(self.stmt, self.data)
        main.connection.execute_stmt(self.stmt, self.data)
        return ("New seed added to Database")
