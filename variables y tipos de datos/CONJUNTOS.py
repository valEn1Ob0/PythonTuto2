conjunto = {1, 'nombre', True} # definimos el conjunto con algun dato
print(conjunto) # los conjuntos no se pueden acceder por su indice. Como resultado da un error
 
# los conjuntos se puede modificar pero solo el conjunto entero
conjunto = {1, 2, 3}
print(conjunto)

# los conjuntos no permiten elementos duplicados
conjunto = {1, 2, 3, 3}
print(conjunto) # como resultado se elimina el elemento duplicado