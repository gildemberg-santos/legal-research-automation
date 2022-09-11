# -*- coding: utf-8 -*-
# from src.read_pdf import ReadPDF

# search = "00423113820008140301"
# document = ReadPDF('data/DJ SE 5869 28-07-2022.pdf').read_pdf(full_file=True)
# print(document)
# processes = document.split('PROCESSO: ')
# number_of_processes = len(processes)

# for i in range(number_of_processes):
#     if processes[i].find(search) != -1:
#         print("========================================")
#         print(processes[i])

# Teste com o Github
#teste 2
from src.read_pdf import ReadPDF

list_name_file = ['arquivo1.pdf', 'arquivo2.pdf', 'arquivo3.pdf']

for name_file in list_name_file:
    document = ReadPDF(f'./data/{name_file}')
    document.save_txt(f'./data/{name_file}.txt')


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Label(frm, text="Gildemberg Santos Gomes").grid(column=0, row=1)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
