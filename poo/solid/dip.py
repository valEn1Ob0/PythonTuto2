# DIP (Principio de Inversión de Dependencias),
# 1. Los modulos de alto nivel (cómponentes que definen el funcionamiento del sistema),
# no deben depender de los modulos de bajo nivel (cómponentes que definen un funcionamiento específico) sino que ambos deben depender de las abstracciones
# 2. Las abstracciones no deben depender de interfaces específicas sino al revés

# EJEMPLO EQUIVOCADO ❌, la clase CorrectorOrtográfico no debe depender de una clase de bajo nivel como Diccionario sino de una abstracción
class Diccionario:
    def verificar_palabra(self, palabra):
        pass


class CorrectorOrtográfico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        pass


from abc import ABC, abstractmethod

# EJEMPLO CORRECTO ✅, en este caso CorrectorOrtográfico no depender de ningún módulo de bajo nivel, sino de la abstracción,
# que puede ser con cualquier clase que herede de una clase abstracta
class VerficadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass


class Diccionario(VerficadorOrtografico):
    def verificar_palabra(self, palabra):
        pass


class CorrectorOrtográfico:
    def __init__(self, verificador):
        self.verificado = verificador

    def corregir_texto(self, texto):
        pass
