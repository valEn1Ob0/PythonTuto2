"""
Este archivo explica cómo utilizar la librería `typing` para hacer
anotaciones de tipo más expresivas y robustas en Python. Esto permite
describir estructuras de datos complejas y ayuda a herramientas como
mypy, Pyright o IDEs para detectar errores de tipo sin ejecutar el código.

IMPORTANTE: Aunque desde Python 3.9+ se pueden usar tipos genéricos con
la sintaxis nativa (ej. `list[int]`), `typing` sigue siendo ampliamente
utilizado por compatibilidad o por su expresividad (ej. `Union`, `Any`, etc).
"""

from typing import List, Dict, Tuple, Set, Union, Optional, Any, Callable, Literal

# Lista de enteros
numeros: List[int] = [10, 20, 30, 40]

# Lista de strings
nombres: List[str] = ["Alice", "Bob", "Charlie"]

# Diccionario con claves de tipo string y valores de tipo int
inventario: Dict[str, int] = {
    "tornillos": 100,
    "tuercas": 250
}

# Tupla de tamaño fijo: (nombre, edad)
persona: Tuple[str, int] = ("skibidi", 21)

# Set de strings
lenguajes_favoritos: Set[str] = {"Python", "C", "Rust"}

# Union: puede ser int o str
codigo: Union[int, str] = "X123"

# Optional: puede ser float o None
descuento: Optional[float] = None

# Any: tipo completamente dinámico, sin validación
dato_desconocido: Any = [1, "dos", {"tres": 3}]

# Literal: acepta solo valores específicos (útil para constantes)
estado_actual: Literal["activo", "inactivo", "pendiente"] = "activo"

# Representa una función que toma dos enteros y devuelve un float
operacion: Callable[[int, int], float]

# Ejemplo de variable con un tipo aún no inicializado
# (no es obligatorio asignar el valor en el momento de la anotación)
resultado_final: Optional[int]

# Tupla anidada: coordenadas (latitud, longitud) con un nombre
ubicacion_marcada: Tuple[str, Tuple[float, float]] = ("Casa", (-34.6, -58.4))

# Diccionario complejo: persona con campos variados
persona_detallada: Dict[str, Union[str, int, bool]] = {
    "nombre": "skibidi",
    "edad": 21,
    "estudiante": True
}