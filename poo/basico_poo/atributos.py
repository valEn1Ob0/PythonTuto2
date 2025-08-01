class Celular:
    def __init__(self, marca, modelo, camara): # método especial que inicializa el objeto al crearlo
        # Aca se definen los atributos del objeto usando self para referenciar a la identidad del objeto mismo
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

print(celular2.marca)