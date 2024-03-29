import PyPDF2
import re
import codecs

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