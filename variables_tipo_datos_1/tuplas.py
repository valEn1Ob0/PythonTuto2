tupla = (1, 2, 3) # definimos la tupla con algún dato
print(tupla[0]) # imprimimos la lista con su índice 0 y el elemento 1 (el índice siempre empieza de 0)

# las tuplas permiten elementos duplicados
tupla = (1, 2, 3, 3)
print(tupla)

# la tupla no se puede modificar a menos que la modifiques completamente
tupla = (4, 5, 6)
tupla[2] = "cambio" # como resultado me va a dar un error