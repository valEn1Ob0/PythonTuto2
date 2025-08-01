# LCP (Principio de Sustitución de Liskov) cualquier instancia de una subclase debe poder hacer lo mismo que hace una instancia de la clase padre,
# sin alterar las expectativas declaradas en la clase padre

# EJEMPLO EQUIVOCADO ❌, la clase Pinguino no puede hacer todo lo que hace la clase padre
class Ave:
    def volar(self):
        return "Estoy volando"


class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"


def hacer_volar(ave=Ave):
    return ave.volar()

# EJEMPLO CORRECTO ✅, cada instancia de las subclases de Ave puede hacer lo mismo que cualquier instancia de la clase Ave,
# sin alterar las expectativas declaradas en la clase padre
class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "No puedo volar"


class AveNoVoladora(Ave):
    pass
