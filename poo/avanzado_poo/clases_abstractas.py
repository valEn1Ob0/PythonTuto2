from abc import ABC, abstractclassmethod


class Persona(ABC):  # esta clase no se puede instanciar, ya que es una clase abstracta que actúa como "receta" para las clases hijas

    # Los siguientes metodos con el decorador "abstractclassmethod" son metodos abstractos, o sea que todavía no tienen ninguna implementación,
    # que las clases hijas las tienen que implementar obligatoriamente
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

# Estas son las clases abstractas
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de {self.actividad}")


dalto = Estudiante("Lucas", 21, "Masculino", "programación")
pedrito = Trabajador("Pedrito", 25, "No binario", "programación")
dalto.hacer_actividad()
pedrito.presentarse()