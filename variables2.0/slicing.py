cadena = "123456789"

print(cadena[0]) # acceso normal

print(cadena[1:3]) # accede al elemento seleccionado detras del doble punto y al elemento despues del doble punto - 1

print(cadena[:]) # si no se especifica se acceden a todos los elementos del array

print(cadena[:-1]) # accede desde el final del array hacia el comienzo del array, el final del array comienza con -1 y va hacia atras

print(cadena[::1]) # el segundo punto determina como recorre el array, 1 por 1, 2 por 2, -1 (osea de atras para adelante)

print(cadena[::-1]) # el segundo punto determina como recorre el array, 1 por 1, 2 por 2, -1 (osea de atras para adelante)