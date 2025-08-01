class Animal:
    def comer(self):
        print("El animal está comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Mamífero(Animal):
        def amamantar(self):
            print("El animal está amamantando")

class Murciélago(Mamífero, Ave):
    pass

murciélago = Murciélago()

murciélago.comer()
murciélago.amamantar()
murciélago.volar()