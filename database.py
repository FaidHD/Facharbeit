import mysql.connector


class Connection:

    def __init__(self, hostname, database, username, password):
        self.hostname = hostname
        self.database = database
        self.username = username
        self.password = password
        self.connection = mysql.connector.connect(  # Verbindung zur Datenbank aufbauen und diese speichern
            host=self.hostname,
            database=self.database,
            user=self.username,
            password=self.password
        )

    def execute_stmt(self, statement, values=None):  # Methode zur reinen Ausführung von SQL Befehlen ohne Rückgabe
        cursor = self.connection.cursor()
        if values is not None:  # Fallunterscheidung, ob zugehörige Werte gegeben sind
            cursor.execute(statement, values)  # Vorbereitung des SQL Befehls mit gegebenen Werten
        else:
            cursor.execute(statement)  # Vorbereitung des SQL Befehls ohne gegebene Werte
        self.connection.commit()  # Ausführung der eingegebenen Befehle

    def qry_stmt(self, statement, values=None):  # Methode zur Ausführung von SQL Befehlen mit Rückgabe
        cursor = self.connection.cursor()
        if values is not None:  # Fallunterscheidung, ob zugehörige Werte gegeben sind
            cursor.execute(statement, values)  # Vorbereitung des SQL Befehls mit gegebenen Werten
        else:
            cursor.execute(statement)  # Vorbereitung des SQL Befehls ohne gegebene Werte
        result = cursor.fetchall()  # Abrufen der Rückgabewerte der Datenbank
        return result  # Rückgabe der Daten

    def close(self):
        self.connection.close()  # Schließen der Verbindung zur Datenbank
