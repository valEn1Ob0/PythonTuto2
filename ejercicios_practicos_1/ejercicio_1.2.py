frase = input('decime una frase y te calculo cuantas palaras dijiste: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras} de palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirlo')
print(f'dalto lo diria en {cantidad_de_palabras/3*1.3}')
if cantidad_de_palabras > 120:
    print('\nboe tantas palabras')