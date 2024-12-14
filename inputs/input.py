# El input pide datos al usuario y almacena el nombre en una variable
nombre = str(input("Dame tu nombre ameo: "))
empieza_con = nombre.startswith("Ti")

if empieza_con:
    print('Tu nombre empieza con Ti')
else:
    print('No sé cómo empieza tu nombre')

