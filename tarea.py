import os

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def divicion(a, b):
    return a / b
try:
    opciones = int(input("ingrese la cantidad de operaciones a hacer: "))
except ValueError:
    print("error valor")
contador = 0
while contador < opciones:    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1 para hacer una suma")
        print("2 para hacer una resta")
        print("3 para hacer una división")
        print("4 para salir")
        opcion = int(input("ingrese una operacion: "))
        if opcion == 4:
            print("gracias por usar la calculadora")
            break
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        

        if opcion == 1:
            print(f"el resultado es: {suma(num1, num2)}") 
            contador += 1
        elif opcion == 2:
            print(f"el resultado es: {resta(num1, num2)}")
            contador += 1
        elif opcion == 3:
            print(f"el resultado es: {divicion(num1, num2)}")
            contador += 1
        
    except ValueError as e:
        print(e)
    except ZeroDivisionError as er:
        print(er) 