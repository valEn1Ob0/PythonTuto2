def sumar_inputs():
    while True:
        try: # prueba si es entero
            a = int(input("numero 1: "))
            b = int(input("numero 2: "))
        except ValueError as e: # si hay un error de valor se imprime el codigo del error en la consola
            print(f"ERROR {e}")
        else: # si no hay error y se termina el try, se acaba el bucle while
            break
        finally: # esto se ejecuta siempre
            print("esto se ejecuta siempre")

    resultado = a + b
    return resultado

print(sumar_inputs())
