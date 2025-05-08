# falto el profe y los alumnos arman la clase

# se pide el nombre y la edad de los compañeros que fueron a clase
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = str(input("ingrese el nombre del compañero: "))
        edad = int(input("ingrese la edad de los compañeros: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(3)

print(f"el profesor es {profesor} y su asistente es {asistente}")
