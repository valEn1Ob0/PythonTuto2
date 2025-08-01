# SRP (Principio de Responsabilidad Unica), cada clase debe tener un solo propósito

# EJEMPLO EQUIVOCADO ❌, la clase Auto se encarga de la creación y movimiento + gestión del combustible
class Auto:
    def __init__(self):
        self.posición = 0
        self.combustible = 100

    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posición += distancia
            self.combustible -= distancia / 2
        else:
            print("no hay suficiente combustible")

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    

# EJEMPLO CORRECTO ✅, la clase Auto SOLO se encarga de la creación y movimiento +
# la clase TanqueDeCombustible SOLO se encarga de la gestión del combustible
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


class Auto:
    def __init__(self, tanque):
        self.posición = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posición += distancia
            self.tanque.usar_combustible(distancia / 2)
            print(f"te queda: {self.tanque.obtener_combustible()} combustible")
        else:
            print("no hay suficiente combustible")

    def obtener_posición(self):
        return self.posición


tanque = TanqueDeCombustible()
autito = Auto(tanque)

for i in range(10):
    autito.mover(10)
    print(f"posición: {autito.obtener_posición()}\n")
