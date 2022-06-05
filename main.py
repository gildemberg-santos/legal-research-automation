# -*- coding: utf-8 -*-
from src.read_pdf import ReadPDF

search = "00423113820008140301"
document = ReadPDF(
    'data/DJ.pdf').read_pdf(full_page=True, page_number=0)
processes = document.split('PROCESSO: ')
number_of_processes = len(processes)

for i in range(number_of_processes):
    if processes[i].find(search) != -1:
        print("========================================")
        print(processes[i])
