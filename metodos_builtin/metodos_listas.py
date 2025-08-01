# se crea una lista con "list"
lista = list([5,4,True])

print(lista)

# nos permite saber la cantidad de elementos que tiene la lista 
elementos_lista = len(lista)

print(elementos_lista)

# agrega elementos a la lista
lista.append(1)

print(lista)

# agrega un elemento a la lista con un indice especifico
lista.insert(0,20)

print(lista)

# agrega varios elementos a la lista en la última posición
lista.extend([10, False, 12, 13,5])

print(lista)

# elimina elementos de la lista (por su índice)
lista.pop(0)

print(lista)

# remueve un elemento de la lista por su nombre
lista.remove(12)

print(lista)

# ordena los elementos de forma ascendente
lista.sort()

print(lista)

# ordena los elementos de forma descendente
lista.sort(reverse=True)

print(lista)

# invierte los elementos de una lista
lista.reverse()

print(lista)

# elimina toda la lista
lista.clear()

print(lista)