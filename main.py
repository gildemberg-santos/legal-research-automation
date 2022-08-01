# -*- coding: utf-8 -*-
from src.read_pdf import ReadPDF

# search = "00423113820008140301"
document = ReadPDF('data/DJ SE 5869 28-07-2022.pdf').read_pdf(full_file=True, page_number=0)
print(document)
# processes = document.split('PROCESSO: ')
# number_of_processes = len(processes)

# for i in range(number_of_processes):
#     if processes[i].find(search) != -1:
#         print("========================================")
#         print(processes[i])

# Teste com o Github
#teste 2