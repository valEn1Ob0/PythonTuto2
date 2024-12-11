diccionario = {
    'clave1':123,
    'clave2':456,
    'clave3':789
}

# muestra las claves del diccionario
claves = diccionario.keys()

print(claves)

# devuelve el valor de las claves cuando se las menciona (si no se encuantra la clave el programa continua)
valor_claves = diccionario.get('clave1')

print(valor_claves)

# elimina un elemento del diccionario con su identificación (coma para sacar mas elementos)
diccionario.pop('clave1')

print(diccionario)

# recorre el diccionario para acceder a cada uno de los elementos
diccionario_iterable = diccionario.items()

print(diccionario_iterable)

# elimina todos los elementos de la lista
diccionario.clear()

print(diccionario)