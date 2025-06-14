import pandas as pd
import matplotlib.pyplot as plt # libreria basica y versatil para visualizar graficos
import seaborn as sns # misma idea que matplotlib pero optimizada para trabajar con pandas y con graficos estadisticos

df = pd.read_csv("pedos.csv")

sns.lineplot(x="fecha",y="pedos",data=df) # dibuja los valores sobre columnas en el eje cartesiano con el df como la fuente de los valores

plt.plot("08-01",9,"o") # marca a el pico del grafico con un punto

plt.show() # muestra el grafico