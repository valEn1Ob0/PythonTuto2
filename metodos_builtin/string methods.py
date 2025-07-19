texto = "texto,de,strings"
texto1 = "texto2"

# muestra todos los metodos de cada tipo
dire = dir(texto)

print(dire)

# convierte texto a mayusculas
mayusc = texto.upper() 

print(mayusc)

# convierte texto a minuscula
minusc = texto.lower() 

print(minusc)

""" 
convierte la primera letra del texto a mayusculas 
(convierte toda la cadena de texto en minuscula y luego la primera letra a mayuscula)
"""
primer_letra_mayusc = texto.capitalize()

print(primer_letra_mayusc)

"""
busca una cadena de texto dentro de esa cadena de texto
(deevuelve un numero el cual indica la posición de la cadena de 
texto desde cero y si no encuentra nadade vuelve -1)
"""
encontrar = texto.find("texto1")

print(encontrar)

# busca una cadena dentro de otra cadena (si no encuentra la cadena de texto da un error)
busqueda_index = texto.index("o")

print(busqueda_index)

# si es numerico devuelve "true", sino devuelve "false"
es_numerico = texto.isnumeric()

print(es_numerico)

# si es alphanumerico devuelve "true", sino devuelve "false"
es_alphanumerico = texto.isalpha()

print(es_alphanumerico)

# cuenta la cantidad de veces que se repite una cadena de texto dentro de otra cadena de texto
contar_coincidencias = texto.count("t")

print(contar_coincidencias)

# cuenta cuantos caracteres tiene una cadena (len no es un metododo sino una función)
contar_caracteres = len(texto)

print(contar_caracteres)

# checkea si una cadena empieza con otra cadena dada, si es asi devuelve "true"
empieza_con = texto.startswith("sg")

print(empieza_con)

# checkea si una cadena termina con otra cadena dada, en ese caso devuelve "true"
termina_con = texto.endswith("gs")

print(termina_con)

# remplaza un pedazo de una cadena por otra cadena de texto
cadena_nueva = texto1.replace(" ","nose")
cadena_nueva_2 = cadena_nueva.capitalize()

print(cadena_nueva_2)

# separar cadenas con las nuevas que le pasemos para crear un array
cadena_separada = texto.split("t")

print(cadena_separada)