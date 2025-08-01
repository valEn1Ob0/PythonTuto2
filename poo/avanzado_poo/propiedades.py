class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property # puedo usar a este método como atributo
    def nombre(self):
        return self.__nombre

    @nombre.setter # ahora también puedo modificar el atributo
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter # esta es la interfaz pública para poder eliminar el atributo
    def nombre(self):
        del self.__nombre


dalto = Persona("dalto", 21)
print(dalto.nombre)

dalto.nombre = "pepe"
print(dalto.nombre)

del dalto.nombre