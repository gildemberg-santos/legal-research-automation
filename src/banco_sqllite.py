import sqlite3
from sqlite3 import Error

# Classe responsavel por criar o banco de dados com as informações dos jornais


class Banco(object):
    # Salva o arquivo PDF em sqlite db (numero da pagina, nome do arquivo, texto)
    # função para criar conexão com banco de dados
    # cria banco SQLite do Python

 # cria banco SQLite do Python
    def __init__(self) -> None:
        self.conn = None

    def open_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def __execute(self,query):
        try:
            c = self.conn.cursor()
            c.execute(query)
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        self.__execute(create_table_sql)

    def insert_data(self, insert_table_sql):
        self.__execute(insert_table_sql)

    def select_data(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM jornais")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def close_connection(self):
        self.conn.close()
    

if __name__ == '__main__':
    db = Banco()
    db.open_connection(r"./db/pjur.db")

    sql_jornais_create = """ 
        CREATE TABLE IF NOT EXISTS jornais (
            id integer PRIMARY KEY,
            n_page integer,
            nome_jornal text,
            texto text,
            create_date text,
            update_date text
        ); """
    
    sql_jornais_insert = ''' INSERT INTO jornais(n_page,nome_jornal,texto,create_date,update_date)
              VALUES(?,?,?) '''

    db.create_table(sql_jornais_create)
    db.close_connection()
