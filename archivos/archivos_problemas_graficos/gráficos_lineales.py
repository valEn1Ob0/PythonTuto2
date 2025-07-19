import pandas as pd
import matplotlib.pyplot as plt # libreria básica y versátil para visualizar gráficos
import seaborn as sns # misma idea que matplotlib pero optimizada para trabajar con pandas y con gráficos estadísticos

df = pd.read_csv("pedos.csv")

sns.lineplot(x="fecha",y="pedos",data=df) # dibuja los valores sobre columnas en el eje cartesiano con el df como la fuente de los valores

plt.plot("08-01",9,"o") # marca al pico del gráfico con un punto

plt.show() # muestra el gráfico