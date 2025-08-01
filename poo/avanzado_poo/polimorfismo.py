class Animal:
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"


class Perro(Animal):
    def sonido(self):
        return "Guau"


gato = Gato()
perro = Perro()

def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(perro) # aca se usa el mismo método para cualquier objeto pasado