# creando una función simple
#def saludar():
#    print("hola")
#
#saludar()
#saludar()
#saludar()
#
# o también
#print("")
#
#for _ in range(3):
#    saludar()


# función con parámetros
def saludar(nombre):
    print(f"hola, {nombre}")

saludar("juan")

# función con un retorno
def encriptar(num):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    contraseña = chars[num % len(chars)]
    return contraseña
    
def desencriptar(caracter):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for índice, elemento in enumerate(chars):
        if elemento == caracter:
            return índice + 1
    return None


encriptar = encriptar(123)
desencriptar = desencriptar(1)
print(encriptar)
print(desencriptar)