from logging import exception
from pickle import NONE
import sqlite3
from sqlite3 import Error

# Classe responsavel por criar o banco de dados com as informações dos jornais

class Banco(object):
    # Salva o arquivo PDF em sqlite db (numero da pagina, nome do arquivo, texto)
    # função para criar conexão com banco de dados

 # cria banco SQLite do Python e tabelas
    def __init__(self) -> None:
        self.conn = None
        self.__identify_type()

    def open_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def __execute(self, query,values = None):
        try:
            self.__identify_type(values)
            c = self.conn.cursor()
            if values:
                c.execute(query,values)
            else: 
                c.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        self.__execute(create_table_sql)

    def insert_data(self, insert_table_sql,values):
        self.__execute(insert_table_sql,values)
       
    def select_data(self,select_table_sql):
        
        try:
            self.__identify_type()
            cur = self.conn.cursor()
            cur.execute(select_table_sql)
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)
            return([])

    def delete_data(self,delete_table_sql,id):
        self.__execute(delete_table_sql,id)
    
    def __identify_type(self, values = None):
        if not (type(values) == tuple or values == None):
            raise Exception('Tipo de dado inválido')

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
              VALUES(?,?,?,?,?) '''
    sql_jornais_select = ''' SELECT * FROM jornais '''  
    sql_jornais_delete = ''' DELETE FROM jornais WHERE id=? '''           
    values_jornais = (55,"alexandre","jhdgsgdsjhgsdj","","")

    db.create_table(sql_jornais_create)
    db.insert_data(sql_jornais_insert,values_jornais)
    db.delete_data(sql_jornais_delete,3)
    select_dados = db.select_data(sql_jornais_select)
    for item in select_dados:
        print(item)
    db.close_connection()

