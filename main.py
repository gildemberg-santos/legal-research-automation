import os
from src.read_pdf import ReadPDF
from src.file import File

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

cls()
print('Listando arquivos PDF\n')
files = File('./').get_files()
for i in range(len(files)):
    print(f'    [{i}] - {files[i]}')
file = int(input('\nDigite o número do arquivo PDF para ler: '))

cls()
print (f'Arquivo selecionado: {files[file]}')
print('\nEscolha uma opção:\n')
print('    [1] - Ler todo o arquivo')
print('    [2] - Ler uma página específica')
option = int(input('\nDigite a opção: '))

# Inicializa a classe ReadPDF

cls()
print('Lendo arquivo PDF ...\n')
