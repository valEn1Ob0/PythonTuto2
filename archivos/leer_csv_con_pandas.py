import pandas as pd

# df = pd.read_csv("archivos\\datos_comas.csv",names=["name","lastname","age"]) # almacena el dato leido como un dataframe que es filas y columnas mas un encabezado

df = pd.read_csv("datos_comas.csv")
df2 = pd.read_csv("datos_comas.csv")

nombre = df["nombre"]  # obtiene los datos de la columna nombre

df_ordenado_asendente = df.sort_values("edad")  # ordena la fila de forma asendente (menor a mayor)
df_ordenado_desendente = df.sort_values("edad",ascending=False)  # ordena la fila de forma desendente (mayor a menor)

df_concatenado = pd.concat([df,df2]) # me concatena los dos dataframes reservando nuevas columnas para estos

primer_fila = df.head(1) # almacena desde la primer columna del dataframe

ultima_fila = df.tail(2) # almacena la desde la ultima columna del dataframe

filas_y_columnas = df.shape # almacena la cantidad de filas y columnas
filas,columnas = df.shape # misma funcion utilizando el desempaquetado para almacenar las variables

df_info = df.describe() # almacena datos utiles del dataframe

elemento_loc = df.loc[1, "nombre"] # almacena el elemento especifico (primero se selecciona el indice de la fila y luego el nombre de la columna)

elemento_iloc = df.iloc[1,1] # almacena el elemento especifico (primero se selecciona el indice de la fila y luego el indice de la columna)
nombres = df.iloc[:,0] # almacena todos los nombres

print(nombres)
