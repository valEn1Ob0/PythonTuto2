import pandas as pd
import matplotlib.pyplot as plt # libreria basica y versatil para visualizar graficos
import seaborn as sns # misma idea que matplotlib pero optimizada para trabajar con pandas y con graficos estadisticos

df = pd.read_csv("dispercion.csv")

sns.scatterplot(x="tiempo",y="dinero",data=df) # dibuja los valores sobre columnas en el eje cartesiano con el df como la fuente de los valores

plt.show() # muestra el grafico