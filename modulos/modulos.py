import modulos_saludar # importa un modulo con este nombre
# import modulos_saludar as mds importa el modulo con el nombre especificado
# from modulos_saludar import saludar importa objetos especificos del modulo sin tener que usar el nombre del modulo
# tambien se puede agregar una , y segir añadiendo modulos

import paquete.arigmetica as arigmetica # forma recomendada de importar  subcarpetas 

a = modulos_saludar.saludar("juan") # usa algun objeto del modulo

print(dir(modulos_saludar)) # muestra todos los objetos de un modulo

print(__name__) # dice como se esta ejecutando el archivo, si devuelve en la terminal __main__ signfica que esta ejecutandose directamente, sino, devuelve la ruta del modulo

print(arigmetica.suma(1,2)) # 3