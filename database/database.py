import mysql.connector


class Connection:

    def __init__(self, hostname, database, username, password):
        self.connection = None
        self.cursor = None
        self.hostname = hostname
        self.database = database
        self.username = username
        self.password = password

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.hostname,
            database=self.database,
            user=self.username,
            password=self.password
        )
        self.cursor = self.connection.cursor()

    def execute_stmt(self, statement, values):
        self.cursor.execute(statement, values)

    def execute_stmt(self, statement):
        self.cursor.execute(statement)

    def qry_stmt(self, statement, values):
        self.cursor.execute(statement, values)
        return self.cursor.fetchall()

    def qry_stmt(self, statement):
        self.cursor.execute(statement)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    con = Connection(
        hostname="db.faidhd.de",
        database="facharbeit",
        username="facharbeit",
        password="PhVS_-T0nNc7*K3]",
    )
    con.connect()
    con.execute_stmt("CREATE TABLE IF NOT EXISTS test(`test` INT);")
    con.close()
