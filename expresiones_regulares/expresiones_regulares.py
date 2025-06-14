import re

texto = """Hola esta es una expresion regular @ 1 xd, BLablabla blablabla blablabla. Polno
lorem ipsum dolor 21 sit amet, consectetur adipiscing elit .
linea 3. final papu abababab
"""

resultado = re.search("blablabla",texto) # busca la expresion en el texto seleccionado y la devuelve como un objeto si esta o como None

resultado2 = re.findall("blablabla",texto) # busca todas las coincidencias de la expresion en el texto seleccionado y las devuelve como una lista

resultado3 = re.findall("blablabla",texto,re.IGNORECASE) # lo mismo que la anterior pero no es case sensitive

# \d -> busca digitos numericos del 0-9
resultado4 = re.findall(r"\d",texto) # se usa el r al principio para indicar que es una expresion regular
# \D -> al hacer mayusucla busca el contrario a la expresion normal
resultado5 = re.findall(r"\D",texto)

# \w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado6 = re.findall(r"\w",texto)
resultado7 = re.findall(r"\W",texto) # busca caracteres no alfanumericos

# \s -> busca espacios en blanco [espacios, tabs, saltos de linea]
resultado8 = re.findall(r"\s",texto)

# . -> busca cualquier caracter menos saltos en linea
resultado9 = re.findall(r".",texto)

# \n -> busca saltos de linea
resultado10 = re.findall(r"\n",texto)

# \ -> cancela caracteres especiales
resultado11 = re.findall(r"\.",texto)

resultado12 = re.findall(r"\d\.\s",texto) # en este caso se busca digitos, segido de un punto y un espacio

# ^ -> busca el inicio de una linea
resultado13 = re.findall(r"^",texto)
resultado14 = re.findall(r"^Hola",texto) # busca la expresion en el texto seleccionado
resultado15 = re.findall(r"^lorem",texto,flags=re.M) # interpreta el texto despues del "\n" como una nueva linea

# $ -> busca el final de una linea
resultado16 = re.findall(r"$",texto)
resultado17 = re.findall(r"papu$",texto)
resultado18 = re.findall(r"Polno$",texto,flags=re.M)

# {n} -> busca la expresion n veces en una cadena
resultado19 = re.findall(r"\d{2}",texto)

# {n,m} -> busca la expresion entre n y m veces en una cadena
resultado20 = re.findall(r"\d{2,4}",texto)
resultado21 = re.findall(r"ab{2,4}",texto) # busca la expresion empezando de la a hasta que b entre 2 y 4 veces
resultado22 = re.findall(r"(ab){2,4}",texto) # busca el grupo de la expresion cierta cantidad de veces
resultado23 = re.findall(r"(ab){2}",texto) # busca el grupo de la expresion cierta cantidad de veces
resultado24 = re.findall(r"[ab]{2}",texto) # similar al anterior pero no importa el orden

# | -> busca una cosa o la otra similar a un or logico
resultado25 = re.findall(r"\d{2,4}|lorem",texto)

print(resultado25)
