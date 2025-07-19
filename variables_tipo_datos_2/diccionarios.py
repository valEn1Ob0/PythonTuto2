# creamos un diccionario con dict(), la cual tiene que usarse el = para dar el valor a la clave
diccionario1 = dict(nombre="maxi",apellido="rojos")
print(diccionario1)

# las listas no pueden ser claves, en cambio, las tuplas si lo pueden
diccionario1 = {(1, 2): "numeros"}
print(diccionario1)

# pero si usamos "frozenset()" si se puede usar una lista
lista = frozenset(["lista1", "lista2"])
diccionario1 = {lista: "Xd"}

print(diccionario1)

# creamos un diccionario sin valores con "fromkeys()" 
diccionario1 = dict.fromkeys(["nombre1","nombre2"])

# creamos un diccionario con el valor de "nose" para cada clave con
diccionario1 = dict.fromkeys(["nombre1","nombre2"],"nose")

print(diccionario1)