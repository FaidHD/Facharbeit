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

    def execute_stmt(self, statement, values=None):
        cursor = self.connection.cursor()
        if values is not None:
            cursor.execute(statement, values)
        else:
            cursor.execute(statement)
        self.connection.commit()

    def qry_stmt(self, statement, values=None):
        cursor = self.connection.cursor()
        if values is not None:
            cursor.execute(statement, values)
        else:
            cursor.execute(statement)
        result = cursor.fetchall()
        return result

    def close(self):
        self.connection.close()
