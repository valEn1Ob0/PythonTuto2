class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __str__(self):
        return f"Personaje(nombre={self.nombre}, fuerza={self.fuerza}, velocidad={self.velocidad})"

    def __add__(self, other):
        nuevo_nombre = f"{self.nombre} - {other.nombre}"
        nueva_fuerza = round(((self.fuerza + other.fuerza) / 2) ** 2)
        nueva_velocidad = round(((self.velocidad + other.velocidad) / 2) ** 2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku", 10000, 5000)
vegeta = Personaje("Vegeta", 9000, 3000)
gogeta = goku + vegeta

print(goku)
print(gogeta)
