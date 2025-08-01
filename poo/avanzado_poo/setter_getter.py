class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self): # esta es la interfaz pública para acceder el valor de un atributo privado o muy privado
        return self.__nombre

    def set_nombre(self, nombre): # esta es la interfaz pública para cambiar el valor de un atributo privado o muy privado
        self.__nombre = nombre


dalto = Persona("dalto", 21)
dalto.set_nombre("papo")
print(dalto.get_nombre())