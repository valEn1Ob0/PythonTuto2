# creando mi propia excepción como una clase
class MiExepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")

try:
    raise MiExepcion("Esto es un error") # lanzando mi propia excepción
except MiExepcion as e:
    print(e)