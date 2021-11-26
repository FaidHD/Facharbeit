import main


class create:

    def __init__(self, name, wachszeit, kornabstand, reihenabstand):
        self.con = main.connection

        self.name = name
        self.wachszeit = wachszeit
        self.kornabstand = kornabstand
        self.reihenabstand = reihenabstand
        self.save_data()

    def save_data(self):
        main.connection.execute_stmt(
            "INSERT INTO saat(name, wachszeit, kornabstand, reihenabstand) VALUES('test', 16, 10, 60)")
        return ("New seed added to Database")
