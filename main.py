import os
from src.read_pdf import ReadPDF
from src.file import File

# Função Lambda para limpar o terminal
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

# Bloco responsável por listar os arquivos PDF
cls()
print('Listando arquivos PDF\n')
files = File('./data').get_files()
for i in range(len(files)):
    print(f'    [{i}] - {files[i]}')
file = int(input('\nDigite o número do arquivo PDF para ler: '))

# Bloco responsável por configurar leitura do PDF
cls()
print (f'Arquivo selecionado: {files[file]}')
print('\nEscolha uma opção:\n')
print('    [1] - Ler todo o arquivo')
print('    [2] - Ler uma página específica')
option = int(input('\nDigite a opção: '))

# Inicializa a classe ReadPDF

cls()
print('Lendo arquivo PDF ...\n')
file_name = files[file]
lertodo_pdf = ReadPDF(file_name)
lertodo_pdf.save_txt('./data/teste.txt')
print('pdf tranformado em txt ...\n')