# Los metodos especiales (dunder methods) son metodos definidos por el lenguaje para definir el comportamiento del objeto en diferentes situaciones

class Persona:
    def __init__(self, nombre, edad): # método especial para crear el objeto
        self.nombre = nombre
        self.edad = edad

    def __str__(self): # método especial que devuelve la recreación amigable del objeto en una cadena de texto
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __repr__(self): # método especial que devuelve la recreación técnica del objeto en una cadena de texto
        return f"Persona({self.nombre}, {self.edad})"

    def __add__(self, other): # método especial que sobrecarga el operador "+" para realizar una acción
        nuevo_valor = self.edad + other.edad
        return nuevo_valor

juan_el_mecánico = Persona("juan_el_mecánico", 40)
skibidi = Persona("skibidi", 20)

print(juan_el_mecánico) # __str__

repre = repr(juan_el_mecánico) # __repr__
print(repre)

print(juan_el_mecánico + skibidi) # __add__
