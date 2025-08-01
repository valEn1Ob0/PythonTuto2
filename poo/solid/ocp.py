# OCP (Principio Abierto/Cerrado), las entidades de software tienen que estar abiertas para la extensión pero cerradas para la modificación

# EJEMPLO EQUIVOCADO ❌, la clase Notificador está cerrada para la extensión, ya que obliga a implementar y modificar la versión original de su método "notificar"
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        print(f"Enviando mensaje por un cliente genérico a {self.usuario}")


# EJEMPLO CORRECTO ✅, en la clase Notificador el método "notificar" se puede implementar y modificar externamente sin modificar el método original
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def __init__(self, usuario, mensaje, email):
        super().__init__(usuario, mensaje)
        self.email = email

    def notificar(self):
        print(f"Enviando mensaje por mail a {self.mail}")


class NotificadorSms(Notificador):
    def __init__(self, usuario, mensaje, nro_teléfono):
        super().__init__(usuario, mensaje)
        self.nro_teléfono = nro_teléfono

    def notificar(self):
        print(f"Enviando mensaje por sms a {self.nro_teléfono}")
