class Personas:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def hablar(self):
        print(f"Hola se {self.habilidad}")


class EmpleadoArtista(Personas, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Personas.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa


roberto = EmpleadoArtista("Roberto", 43, "Argentino", "Cantar", 100000, "Microsoft")
roberto.hablar()  # en este caso como hay colisión de métodos usa mro
print(EmpleadoArtista.mro())  # aca se puede ver como se resuelve la colisión de metodos en orden

Artista.hablar(roberto)  # si quiero usar el método de una clase en específico lo hago de esta manera
