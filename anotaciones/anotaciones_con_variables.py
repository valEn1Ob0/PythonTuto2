"""
Este archivo explica qué son las anotaciones de variables en Python
(variable annotations) y cómo se utilizan para mejorar la legibilidad
del código, ayudar a herramientas de análisis estático y facilitar el
desarrollo colaborativo.

Las anotaciones **NO** afectan la ejecución del código en tiempo de
ejecución (a menos que se utilicen con herramientas como mypy o pydantic).
Solo sirven como *pistas* de tipo (type hints).

A partir de Python 3.6, se pueden anotar variables utilizando la sintaxis
Ejemplos más abajo.
"""

# Anotación de variables básicas
nombre: str = "skibidi"
edad: int = 21
altura: float = 1.75
es_estudiante: bool = True


# Anotación sin asignación de valor (se puede hacer, pero es raro fuera de clases)
puntos: int