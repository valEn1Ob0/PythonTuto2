persona = {
    "name": "comidas",
    "cantidad": 30,
    "calorias": 1000
} # definimos el diccionario con algún dato
print(persona["calorias"]) # imprimimos el valor con su clave

# los diccionarios pueden cambiar
persona = {10:20}
print(persona)

# los diccionarios no permiten claves duplicadas
persona = {
    "clave1": 20, 
    "clave1": 10,
    "clave1": -5
}
print(persona) # como resultado usa la clave mas nueva