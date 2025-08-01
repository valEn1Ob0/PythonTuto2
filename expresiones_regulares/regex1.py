import re

text = "The quick brown fox jumps over the lazy dog"

x = re.search("The.*dog$",text) # el * busca cualquier coincidencia

if x:
    print("Se ha encontrado la expresión")
else:
    print("No se ha encontrado la expresión")