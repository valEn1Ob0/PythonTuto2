# Una clase es una guía para crear a un objeto, para definir las características (atributos) y comportamientos (metodos) del objeto
class Celular: # para nombrar clases se usa PascalCase
    # Aca defino atributos estáticos (mismos atributos para cada objeto)
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"

celular1 = Celular() # aca creo una instancia de la clase (objeto), puedo crear tantas instancias como quiera
print(celular1) # me imprime la dirección en la memoria en donde está el objeto
print(celular1.marca) # uso el operador "." para acceder a un atributo o método del objeto