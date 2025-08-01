# creando mi propia excepción como una clase
class MiExepción(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")


try:
    raise MiExepción("Esto es un error") # lanzando mi propia excepción
except MiExepción as e:
    print(e)