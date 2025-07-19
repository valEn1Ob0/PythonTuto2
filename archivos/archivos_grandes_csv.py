import csv

def read_csv_in_chunks(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, chunck in enumerate(reader):
            print(f"Chunck {i}: ")
            print(chunck)

read_csv_in_chunks("archivo_grande.csv")