class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self): # este es un método del objeto, un método define el comportamiento de un objeto
        # Se tiene que pasar el parametro self para que se pueda usar con el operador "."
        print(f"Estas haciendo un llamado de un {self.modelo}")

celular1 = Celular("Samsung", "S23", "48MP")
celular1.llamar()