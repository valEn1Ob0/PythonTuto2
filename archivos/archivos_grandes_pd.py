import pandas as pd


def read_csv_in_chunks(file_name: str) -> None:
    """
    Lee un archivo CSV en bloques (chunks) de 1000 filas y los imprime.

    Parámetros:
    -----------
    file_name : str
        Ruta y nombre del archivo CSV a leer.
    """
    for i, chunk in enumerate(pd.read_csv(file_name, chunksize=1000)):  # itera sobre el archivo en bloques de N cantidad de filas
        print(f"Chunk {i}: ")
        print(chunk)


read_csv_in_chunks("big_file.csv")
