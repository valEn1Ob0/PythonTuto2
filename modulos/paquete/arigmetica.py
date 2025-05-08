def suma(*numeros):
    return sum(numeros)

def resta(*numeros):
    if not numeros:
        return 0
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado -= numero
    return resultado

