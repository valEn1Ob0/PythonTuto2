class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

nombre = str(input("Dígame su nombre: "))
edad = int(input("Ahora su edad: "))
grado = int(input("Ahora su grado: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n
    Nombre: {estudiante.nombre}
    Edad: {estudiante.edad}
    Grado: {estudiante.nombre}
""")

while True:
    estudiar = str(input())
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()