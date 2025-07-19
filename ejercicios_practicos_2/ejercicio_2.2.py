# crear una funcion que nos devuelva los numeros primos
# entre 0 y el argumento que le pasemos

def es_primo(num):
    for i in range(2, num-1):
        if num % 2 == 0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado: primos.append(i)
    return primos
    
primo = primos_hasta(6)
print(primo)