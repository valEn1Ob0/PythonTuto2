person = {
    "name": "comidas",
    "cantidad": 30,
    "calorias": 1000
} # definimos el diccionario con algun dato
print(person["calorias"]) # imprimimos el valor con su clave (solo se puede acceder al valor)

# los diccionarios pueden cambiar pero 
person = {10:20} 
print(person)

# los diccionarios no permiten elementos duplicados para claves
person = {
    "clave1": 20, 
    "clave1": 10,
    "clave1": -5
    }
print(person) # como resultado imprime la clave mas nueva