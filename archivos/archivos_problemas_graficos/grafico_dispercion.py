import pandas as pd
import matplotlib.pyplot as plt # libreria basica y versatil para visualizar graficos
import seaborn as sns # misma idea que matplotlib pero optimizada para trabajar con pandas y con graficos estadisticos

df = pd.read_csv("influenser_ingresos.csv")

sns.barplot(x="fuente",y="ingresos",data=df) # dibuja los valores sobre columnas en el eje cartesiano con el df como la fuente de los valores

total_ingresos = df["ingresos"].sum() # suma todos los valores de la columna y los almacena en una variable

print(f"El total de ingresos es de: {total_ingresos}")

plt.show() # muestra el grafico