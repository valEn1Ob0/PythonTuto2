import pandas as pd

df = pd.read_csv("../datos_comas.csv")
df["edad"] = df["edad"].astype(str) # convierte el dato en strinig

df["nombre"].replace("papu","skibi", inplace=True) # todos los elementos "papu" serán cambiados por "skibi"

df = df.dropna() # elimina las filas que le faltan datos

df = df.drop_duplicates() # elimina las filas duplicadas

df.to_csv("../datos_limpios.csv",index=False,sep=";") # crea un archivo .csv en la ruta sin los índices de las filas y separándolos con punto y coma

print(df)