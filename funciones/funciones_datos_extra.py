def formulario(nombre,apellido,pais):
    return f"hola {nombre}, su apellido es {apellido} y su pais {pais}"

# parametros con palablas clave
relleno = formulario(apellido="pere",nombre="matias",pais="chile")
print(relleno)


# en este caso las palabras clave son valores definidos siempre al final los parametros
def blabla(precios,marca="apple"): 
    return f"la marca: {marca} lanzo su producto a este precio: {precios}"

producto = blabla(10)
print(producto)
