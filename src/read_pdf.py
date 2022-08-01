import PyPDF2
import re


class ReadPDF:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

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
