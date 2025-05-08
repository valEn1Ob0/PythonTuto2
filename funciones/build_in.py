numeros = [10, 1, 7, 8, 9]

numeros_mas_alto = max(numeros)
print(numeros_mas_alto)

nuemro_mas_bajo = min(numeros)
print(numeros_mas_alto)


# redondear a 6 decimales
numero = round(12.456,1)
print(numero)

# duvuelve False si el valor es 0, vacio, False, None
resultado_bool = bool()
print(resultado_bool) # False

# devuelve True si el numero es distinto a 0, True, cadena, datos no vacios
resultado_bool2 = bool([1234])
print(resultado_bool2) # True 

# devuelve True si todos los valores son verdaderos
resultado_all = all([123, True, False])
print(resultado_all) # False

# suma todos los elementos array sino devuelve un error
suma_total = sum(numeros)

print(suma_total)