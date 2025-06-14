# creando mi propia exepcion
class MiExepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")

# lanzando mi propia exepcion
try:
    raise MiExepcion("Esto es un error")
except MiExepcion as e:
    print(e)