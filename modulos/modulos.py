import modulos_saludar # importa un módulo con este nombre
# import modulos_saludar as mds importa el módulo con el nombre especificado
# from modulos_saludar import saludar importa objetos específico del módulo sin tener que usar el nombre del módulo
# también se puede agregar una, y seguir añadiendo modulos

import paquete.aritmética as aritmética # forma recomendada de importar sub carpetas

a = modulos_saludar.saludar("juan") # usa algún objeto del módulo

print(dir(modulos_saludar)) # muestra todos los objetos de un módulo

print(aritmética.__name__) # dice como se está ejecutando el archivo, si devuelve en la terminal __main__ significa que está ejecutándose directamente,
# si no, devuelve la ruta del módulo

print(aritmética.suma(1, 2)) # 3