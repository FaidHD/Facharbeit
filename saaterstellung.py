import main


class Create:

    def __init__(self, name, wachszeit, kornabstand, reihenabstand):
        self.con = main.connection

        print(name, wachszeit, kornabstand, reihenabstand)
        self.data = (name, wachszeit, kornabstand, reihenabstand)
        self.stmt = "INSERT INTO `saat`(`name`, `wachszeit`, `kornabstand`, `reihenabstand`) VALUES (%s,%s,%s,%s)"
        self.save_data()

    def save_data(self):
        print(self.stmt, self.data)
        main.connection.execute_stmt(self.stmt, self.data)
        return "New seed added to Database"

