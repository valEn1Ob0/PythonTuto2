alimentos = ["banana","manzana","pera"]

for alimento in alimentos:
    # ponemos una condicion la cual si se cumple se continua a el siguiente elmento
    if alimento == "banana":
        continue # el "continue" evita todas las operaciones y continua hacia el proximo elemento
    print(f"me como una {alimento}")
for alimento in alimentos:
    # ponemos una condicion la cual si se cumple se cancela el bucle
    if alimento == "banana":
        break # cancela el bucle que se esta ejecutando
    print(f"me como una {alimento}")