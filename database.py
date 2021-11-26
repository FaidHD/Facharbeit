import mysql.connector


class Connection:

    def __init__(self, hostname, database, username, password):
        self.hostname = hostname
        self.database = database
        self.username = username
        self.password = password
        self.connection = mysql.connector.connect(
            host=self.hostname,
            database=self.database,
            user=self.username,
            password=self.password
        )

    def execute_stmt(self, statement, values):
        self.connection.cursor().execute(statement, values)
        self.connection.commit()

    def execute_stmt(self, statement):
        self.connection.cursor().execute(statement)
        self.connection.commit()

    def qry_stmt(self, statement, values):
        self.connection.cursor().execute(statement, values)
        self.connection.commit()
        return self.connection.cursor().fetchall()

    def qry_stmt(self, statement):
        self.connection.cursor().execute(statement)
        self.connection.commit()
        return self.connection.cursor().fetchall()

    def close(self):
        self.connection.close()
