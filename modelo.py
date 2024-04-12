import sqlite3
class AppBD():
    def __init__(self):
        self.create_table()

    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect("database.db")
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados", error)
    
    def create_table(self):
        self.abrirConexao()
        create_table_query = """ CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        ); """

        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Falha ao criar tablea", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexao com o sqlite foi fechada")
    
    def inserirDados(self, name, price):
        self.abrirConexao()
        insert_query = " INSERT INTO products (name, price) VALUES (?, ?); "
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (name, price))
            self.connection.commit()
            print("Produto inserido com sucesso")
        except sqlite3.Error as error:
            print("Falha ao inserir dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexao com o sqlite foi fechada")
    
    def select_all_products(self):
        self.abrirConexao()
        select_query = ''' SELECT * FROM products;'''
        products = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao retornar produtos", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexao com o sqlite foi fechada")
        return products

    def update_products(self, product_id, name, price):
        self.abrirConexao()
        update_query = """ UPDATE products SET name = ?, price = ? WHERE id = ?;"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query, (name, price, product_id))
            self.connection.commit()
            print("Dados atualizados com sucesso")
        except sqlite3.Error as error:
            print("Falha ao alterar dados na tabela", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada")
    
    def delete_products(self, product_id): # definição da função de apagar dados com base no id do produto
        self.abrirConexao() # abre conexão
        delete_query = """ DELETE FROM products WHERE id = ?; """ # comando SQL para deletar um dado de uma tabela
        try: # execução do código
            cursor = self.connection.cursor() # abrindo o cursor parar executar o comando SQL
            cursor.execute(delete_query, (product_id,)) # cursor executando o comando SQL
            self.connection.commit() # Enviando as alterações pro banco de dados
            print("Produto deletado com sucesso") # mensagem de sucesso
        except sqlite3.Error as error: # tratamento de exceção
            print("Erro ao deletar produto", error) # mensagem de erro
        finally: # fechar o cursor e a conexão
            if self.connection: # se a conexão existir
                cursor.close() # fechando o cursor
                self.connection.close() # fechando a conexão 
                print("A conexão com o sqlite foi fechada") # mensagem de fechamento concluido