import main


class Create:

    def __init__(self, name, wachszeit, kornabstand, reihenabstand):
        self.con = main.connection

        self.data = (name, wachszeit, kornabstand, reihenabstand)
        self.stmt = "INSERT INTO `saat`(`name`, `wachszeit`, `kornabstand`, `reihenabstand`) VALUES (%s,%s,%s,%s)"
        self.save_data()

    def save_data(self):
        main.connection.execute_stmt(self.stmt, self.data)
        return "New seed added to Database"

