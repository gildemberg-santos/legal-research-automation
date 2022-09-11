import os

# Classe responsável por manipular arquivos
class File:
    # Construtor da classe
    # Recebe o caminho do diretório
    def __init__(self, path):
        self.path = path
        self.files = []

    # Classe responsável por listar os arquivos PDF
    # Retorna uma lista com os arquivos PDF para a variável files
    def get_files(self, extension: str = 'pdf') -> list:
        if extension:
            ways = [os.path.join(self.path, name)
                    for name in os.listdir(self.path)]
            files = [file for file in ways if os.path.isfile(file)]
            self.files = [
                arq for arq in files if arq.lower().endswith(extension)]
        return self.files
