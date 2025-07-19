import pandas as pd
import matplotlib.pyplot as plt # libreria básica y versátil para visualizar gráficos
import seaborn as sns # misma idea que matplotlib pero optimizada para trabajar con pandas y con gráficos estadísticos

df = pd.read_csv("dispersión.csv")

sns.scatterplot(x="tiempo",y="dinero",data=df) # dibuja los valores sobre columnas en el eje cartesiano con el df como la fuente de los valores

plt.show() # muestra el grafico