import csv

with open('exemplo.csv', 'r',  newline='', encoding= 'utf-8') as file:
    ler_file = csv.reader(file)
    # print(ler_file)
    for linha in ler_file:
       # print(linha)

        if int(linha[1]) >= 18:
            print(f'A pessoa {linha[0]} é velho')