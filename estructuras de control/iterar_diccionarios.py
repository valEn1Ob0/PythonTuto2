diccionario = dict(nombre="pro",apellido="xd")

# recorremos el diccionario con key lo cual mestra las claves
for key in diccionario:
    print(key)

# recorremos el diccionario con "items()" para obtener la clave y el valor
for key in diccionario.items():
    clave = key[0] # si es 0 da el clave
    valor = key[1] # y si es 1 da el valor
    print(f"la clave es {clave} y el valor es {valor}")