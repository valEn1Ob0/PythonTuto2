números = [10, 1, 7, 8, 9]

números_más_altos = max(números)
print(números_más_altos)

número_más_bajo = min(números)
print(números_más_altos)


# redondear a 6 decimales
numero = round(12.456,1)
print(numero)

# devuelve False si el valor es 0, vacío, False, None
resultado_bool = bool()
print(resultado_bool) # False

# devuelve True si el numero es distinto a 0, True, cadena, datos no vacios
resultado_bool2 = bool([1234])
print(resultado_bool2) # True 

# devuelve True si todos los valores son verdaderos
resultado_all = all([123, True, False])
print(resultado_all) # False

# suma todos los elementos array si no devuelve un error
suma_total = sum(números)

print(suma_total)