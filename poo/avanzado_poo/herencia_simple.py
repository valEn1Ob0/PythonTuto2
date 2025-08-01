class Personas:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola")

# LA HERENCIA SIMPLE ES HEREDAR LOS ATRIBUTOS Y METODOS DE UNA CLASE PADRE A UNA O VARIAS CLASES HIJA
class Empleado(Personas):
    # La clase padre se pone en paréntesis
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) # este método define que atributos hereda de la clase padre
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self): # el método se sobreescribe si existe en la clase padre
        print("NO")

roberto = Empleado("Roberto", 43, "Argentino", "Programador", 10000)
roberto.hablar()
