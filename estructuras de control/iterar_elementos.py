numeros = [1,2,6]
comidas = ["carne","huevo","papa"]

# recorremos la lista "numeros" con el indice y valor actual "numero"
for numero in numeros: 
    print(f"el numero ahora es: {numero}")

# recorremos dos listas con el "zip()" (las listas tienen que tener la misma canridad de elementos)
for numero,comida in zip(numeros,comidas): 
    print(f"recorriendo numero {numero}")
    print(f"recorriendo comida {comida}")

# se itera num1 en un rango de 11 (simpre empezando desde 0)
for num1 in range(11):
    print(f"recorriendo numero {num1}")


# se itera el num en el rango de 1 a 5 (el primer número cuenta, pero el segundo no)
for num in range(1, 5): 
    print(f"recorriendo numero {num}")

# forma no optima de recorrer una lista (no funciona en Conjuntos)
for list in range(len(numeros)):
    print(numeros[list])

# forma optima de recorrer la lista
for lisa in enumerate(numeros):
    indice = lisa[0] # si es 0 da el indice
    valor = lisa[1] # y si es 1 da el valor
    print(f"el indice es: {indice} y el valor es: {valor}")

# usamos un "else" para realizar una operación luego del for (si hay un "break" en el for no se cumple esta condición)
for num in numeros:
    print(f"el numero es {num}")
else:
    print("termino tu operacion capo")

# todo esto se puede hacer con: Tuplas, Listas, Conjuntos