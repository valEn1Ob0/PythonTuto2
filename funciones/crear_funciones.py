# creando una funcion simple
#def saludar():
#    print("hola")
#
#saludar()
#saludar()
#saludar()
#
# o tambien
#print("")
#
#for _ in range(3):
#    saludar()


# funcion co parametros
def saludar(nombre):
    print(f"hola, {nombre}")

saludar("juan")

# funcion con un retorno
def encriptar(num):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    contraseña = chars[num % len(chars)]
    return contraseña
    
def desencriptar(charact):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i, elemento in enumerate(chars):
        if elemento == charact:
            return i + 1

encript = encriptar(123)
decript = desencriptar(1)
print(encript)
print(decript)