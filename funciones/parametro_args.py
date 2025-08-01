# manear menos optima de sumar valores
def suma(a, b):
    return a+b

resultado = suma(1,2)
print(resultado)

# otra manera de hacerlo aunque no es la mejor
def suma2(elementos):
    números_sum = 0
    for num in elementos:
        números_sum += num
    return números_sum

resultado2 = suma2([1,2,3])
print(resultado2)

# manera óptima de hacerlo con args
def suma3(*números): # *args captura todos los elementos por posición y los empaqueta en una tupla
    return sum(números)

resultado3 = suma3(1, 2, 3, 4)
print(resultado3)

def clave_valor(**kwargs): # **kwargs captura todos los elementos por palabra y los empaqueta como diccionario
    return kwargs

valores = clave_valor(hola="hola",cha="u")
print(valores)