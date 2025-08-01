class Personas:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

# LA HERENCIA MULTIPLE ES HEREDAR LOS ATRIBUTOS Y METODOS DE MUCHAS CLASE PADRE A UNA O MUCHAS CLASES HIJAS
class EmpleadoArtista(Personas, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Personas.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f"Mi nombre es {self.nombre}, mi habilidad es {super().mostrar_habilidad()} y trabajo para {self.empresa}"
        # en este caso estamos usando un método de la siguiente clase en el mro, si usásemos self usaría el método de la misma clase

roberto = EmpleadoArtista("Roberto", 43, "Argentino", "Cantar", 100000, "Microsoft")
print(roberto.presentarse())

herencia = issubclass(EmpleadoArtista, Artista) # pregunto si la primera clase es una subclase de la segunda clase
instancia = isinstance(roberto, Personas) # pregunto si el objeto es una instancia de la clase

print(instancia)