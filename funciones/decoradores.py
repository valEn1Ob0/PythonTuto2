# Un decorador es una función que "decora" (agrega contenido a la función original antes o después de ejecutarla),
# para crear un decorador: se crea una función, dentro de la función creo otra función que es la función que devuelve el decorador
def decorador(función):
    def función_modificada():
        print("antes de llamar a la función")
        función()
        print("después de llamar a la función")
    return función_modificada

# def ejemplo():
#     print("función en si")

# función_modificada = decorador(ejemplo) # la función modificada ahora está en una variable
# función_modificada()

# Esta es una forma más simple y habitual de usar un decorador
@decorador
def ejemplo():
    print("función en si")

ejemplo()