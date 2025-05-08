import csv

with open("archivos\\datos_comas.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)