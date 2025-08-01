# ISP (Principio de Segregación de Interfaces) los clientes (el que utiliza la interfaz de otra clase) no deberían depender de interfaces
# (forma de los metodos de una clase que obliga a cumplir a quienes la implementan) que no usan

from abc import ABC, abstractmethod

# EJEMPLO EQUIVOCADO ❌, la clase Robot es obligada a usar las interfaces que no necesita
class Trabajador(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")


class Robot(Trabajador):
    def comer(self):
        pass

    def trabajar(self):
        print("El robot esta trabajando")

    def dormir(self):
        pass

# EJEMPLO CORRECTO ✅, reduzco la cantidad de interfaces innecesarias de la clase padre para definir más interfaces con otras clases
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")


robot = Robot()
robot.trabajar()
