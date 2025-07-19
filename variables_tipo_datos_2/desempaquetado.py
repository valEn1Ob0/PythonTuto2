# definimos la variable datos (puede ser tupla o lista)
datos_tupla = ('número1', 'numero2')
datos_lista = ["valor1", "valor2", "valor3"]
datos_diccionario = {
    1: "valor1",
    2: "valor2",
    3: "valor3"
}

""" 
desempaqueto todos los elementos de la lista, 
(si o si tiene que coincidir la cantidad de claves que agreguemos con la de los valores), 
funciona para tuplas y diccionarios también
"""
clave1,clave2,clave3 = datos_lista

print(clave1)

# en este caso uso el operador * para empaquetar todos los elementos como una lista, funciona para tuplas y diccionarios también
args_lista1, *args_lista2 = datos_lista
print(args_lista2)