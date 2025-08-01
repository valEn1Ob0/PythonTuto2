texto = "texto de strings"
texto1 = "texto2"

# muestra todos los métodos de un objeto
métodos = dir(texto)

print(métodos)

# convierte texto a mayúsculas
mayúscula = texto.upper() 

print(mayúscula)

# convierte texto a minúscula
minúscula = texto.lower()

print(minúscula)

""" 
convierte la primera letra del texto a mayúsculas 
(convierte toda la cadena de texto en minúscula y luego la primera letra a mayúscula)
"""
primer_letra_mayúscula = texto.capitalize()

print(primer_letra_mayúscula)

"""
busca una cadena de texto dentro de esa cadena de texto
(devuelve un numero el cual indica la posición de la cadena de 
texto desde cero y si no encuentra nada devuelve -1)
"""
encontrar = texto.find("texto1")

print(encontrar)

# busca una cadena dentro de otra cadena (si no encuentra la cadena de texto da un error)
búsqueda_índice = texto.index("o")

print(búsqueda_índice)

# si es numérico devuelve "true", sino devuelve "false"
es_numérico = texto.isnumeric()

print(es_numérico)

# si es alfanumérico devuelve "true", sino devuelve "false"
es_alfanumérico = texto.isalpha()

print(es_alfanumérico)

# cuenta la cantidad de veces que se repite una cadena de texto dentro de otra cadena de texto
contar_coincidencias = texto.count("t")

print(contar_coincidencias)

# cuenta cuantos caracteres tiene una cadena
contar_caracteres = len(texto)

print(contar_caracteres)

# comprueba si una cadena empieza con otra cadena dada, si es asi devuelve "true"
empieza_con = texto.startswith("sg")

print(empieza_con)

# comprueba si una cadena termina con otra cadena dada, en ese caso devuelve "true"
termina_con = texto.endswith("gs")

print(termina_con)

# remplaza un pedazo de una cadena por otra cadena de texto
cadena_nueva = texto1.replace(" ","nose")
cadena_nueva_2 = cadena_nueva.capitalize()

print(cadena_nueva_2)

# separar cadenas con las nuevas que le pasemos para crear un array
cadena_separada = texto.split("t")

print(cadena_separada)