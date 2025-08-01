archivo_sin_leer = open("archivos\\leid.txt",encoding="UTF-8") # guarda en la variable este archivo ya abierto, puede se que al leer tenga una codificacion erronea asi que hay que cambiarla

# Distintas formas de leer el archivo
archivo = archivo_sin_leer.read() # lee todo el archivo y la almacena en la variable 

liena_1 = archivo_sin_leer.readline() # lee la primer linea y la almacena en la variable

liena_1 = archivo_sin_leer.readline(100) # lee una cantidad de caracteres determinada y la almacena en la variable

liena_1 = archivo_sin_leer.readlines() # lee líneas como array y la almacena en la variable

# cerrar el archivo
archivo_sin_leer.close()

print(liena_1) 