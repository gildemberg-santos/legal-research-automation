import PyPDF2
import re
import codecs
import sqlite3
from sqlite3 import Error

# Classe responsável por ler os arquivos PDF
class ReadPDF:
    # Construtor
    # Recebe o caminho do arquivo PDF
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    # Lê o arquivo PDF
    # Recebe um parâmetro booleano para retornar o arquivo completo
    # Recebe um parâmetro inteiro para retornar uma página específica
    # Retorna uma string com o conteúdo do arquivo
    def read_pdf(self, full_file: bool = True, page_number: int = 0) -> str:
        pdf_file = open(self.file_name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.numPages if full_file else page_number
        parsed = ""
        for i in range(number_of_pages):
            page = read_pdf.getPage(i)
            page_content = page.extractText()
            parsed += ''.join(page_content)
        parsed = re.sub('n', '', parsed)
        return parsed

    # Salva o arquivo PDF em um arquivo de texto
    def save_txt(self, file_output: str) -> None:
        string_file = self.read_pdf(full_file=True)
        file = codecs.open(file_output, 'w', 'utf-8')
        file.writelines(string_file)
        file.close()

    # Salva o arquivo PDF em sqlite db (numero da pagina, nome do arquivo, texto)
    
    # cria banco SQLite do Python
    '''def create_connection(db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


    if __name__ == '__main__':
        create_connection(r"./db/pythonsdb.db")'''
    
    # criando tabela do banco

    def creat_table(conn,create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def main():
        database = "r./db/pythonsdb.db"

        sql_create_jornal_table = """ CREATE TABLE IF NOT EXISTS jornal (
                                        id integer PRIMARY KEY,
                                        name_jornal text NOT NULL,
                                        number_page text,
                                        texto text
                                    ); """
            # create a database connection
        conn = create_connection(database)

            # create table
        if conn is not None:
            # create jornal table
            create_table(conn, sql_create_jornal_table)

        
        else:
            print("Error! cannot create the database connection.")
    
    if __name__ == '__main__':
        main()