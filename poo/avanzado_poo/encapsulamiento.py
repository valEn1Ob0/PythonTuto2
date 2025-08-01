class MiClase:
    def __init__(self):
        # Los atributos privados por conveniencia (accesibles) se escriben con "_" al principio
        self._atributo_privado1 = "Valor secreto 1"
        self._atributo_privado2 = "Valor secreto 2"

        # Los atributos privados no accesibles se escriben con "__" al principio
        self.__atributo_muy_privado1 = "Valor muy secreto 1"
        self.__atributo_muy_privado2 = "Valor muy secreto 2"

    # El encapsulamiento funciona de la misma manera para los metodos
    def _metodo_privado(self):
        pass

    def __metodo_muy_privado(self):
        pass


objeto = MiClase()
print(objeto._MiClase__atributo_muy_privado2) # realmente se puede acceder, pero con esta sintaxis que es poco usada