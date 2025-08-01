class Personas:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola")

# LA HERENCIA JERÁRQUICA ES HEREDAR LOS ATRIBUTOS Y METODOS DE UNA CLASE PADRE A MUCHAS CLASES HIJAS
class Empleado(Personas):
    # La clase padre se pone en paréntesis
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad) # este método inicializa los atributos y metodos de la siguiente clase en el mro
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self): # el método se sobreescribe si existe en la clase padre
        print("NO")
class Estudiante(Personas):
    # La clase padre se pone en paréntesis
    def __init__(self, nombre, edad, nacionalidad, grado, colegio):
        super().__init__(nombre, edad, nacionalidad) # este método define que atributos hereda de la clase padre
        self.grado = grado
        self.colegio = colegio
    def hablar(self): # el método se sobreescribe si existe en la clase padre
        print("OK")
class Jefe(Personas):
    # La clase padre se pone en paréntesis
    def __init__(self, nombre, edad, nacionalidad, horas, empleados):
        super().__init__(nombre, edad, nacionalidad) # este método define que atributos hereda de la clase padre
        self.horas = horas
        self.empleados = empleados
    def hablar(self): # el método se sobreescribe si existe en la clase padre
        print("SI")

roberto = Empleado("Roberto", 43, "Argentino", "Programador", 10000)
roberto.hablar()