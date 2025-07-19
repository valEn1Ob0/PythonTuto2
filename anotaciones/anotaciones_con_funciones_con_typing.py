"""
Este archivo muestra cómo anotar funciones utilizando tipos avanzados
de la librería `typing`, como:

- List, Dict, Tuple
- Union, Optional
- Callable, Literal
- Any

Esto permite definir funciones más expresivas y precisas en cuanto a los tipos
que aceptan y retornan.
"""

from typing import List, Dict, Tuple, Union, Optional, Callable, Literal, Any


def obtener_elementos(palabras: List[str]) -> Dict[str, int]:
    resultado: Dict[str, int] = {}
    for palabra in palabras:
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado


def buscar_usuario(id: Union[int, str]) -> Optional[Dict[str, Any]]:
    base = {
        1: {"nombre": "skibidi", "activo": True},
        "2a": {"nombre": "Ana", "activo": False}
    }
    return base.get(id)


def calcular_total(precios: List[float], impuesto: float) -> float:
    return sum(precios) * (1 + impuesto)


def aplicar_operacion(a: int, b: int, f: Callable[[int, int], float]) -> float:
    return f(a, b)


def obtener_estado(codigo: str) -> Literal["activo", "inactivo", "pendiente"]:
    if codigo.startswith("A"):
        return "activo"
    return "pendiente"


def procesar_datos(data: Any) -> None:
    print("Procesando:", data)
