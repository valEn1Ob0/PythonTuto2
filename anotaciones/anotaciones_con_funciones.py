"""
Este archivo muestra cómo hacer anotaciones de tipo en funciones
usando los tipos integrados de Python (`int`, `str`, `float`, etc.).

Estas anotaciones ayudan a documentar el código, permiten mejores sugerencias
en el editor y son interpretadas por herramientas de análisis estático.
"""


# Anotación de parámetros y tipo de retorno
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"


def sumar(a: int, b: int) -> int:
    return a + b


def dividir(a: float, b: float) -> float:
    return a / b  # No se valida si b es cero, solo muestra el tipo


def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18


# Función sin valor de retorno (solo realiza una acción)
def mostrar_mensaje(mensaje: str) -> None:
    print(f"[INFO] {mensaje}")


# Parámetro con tipo, pero sin retorno especificado (mala práctica, pero válida)
def imprimir_nombre(nombre: str):
    print(f"Nombre: {nombre}")
