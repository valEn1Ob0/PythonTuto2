import pandas as pd

# df = pd.read_csv("archivos\\datos_comas.csv",names=["name","lastname","age"]) # almacena el dato leido como un dataframe que es filas y columnas mas un encabezado

df = pd.read_csv("archivos\\datos_comas.csv")

nombres = df["nombre"] # obtiene los datos de la columna nombre

df_ordenado_asendente = df.sort_values("edad")
df_ordenado_desendente = df.sort_values("edad",ascending=False)

print(df_ordenado_asendente)
