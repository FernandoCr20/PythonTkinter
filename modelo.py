import sqlite3
class AppBD():
    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect("database.db")
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados", error)
    
    def create_table(self):
        try:
            self.abrirConexao()
            create_table_query = """ CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            ); """