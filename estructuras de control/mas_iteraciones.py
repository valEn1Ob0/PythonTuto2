alimentos = ["banana","manzana","pera"]

for alimento in alimentos:
    # ponemos una condición la cual si se cumple se continúa al siguiente elemento
    if alimento == "banana":
        continue # el "continue" evita todas las operaciones y continua hacia el proximo elemento
    print(f"me como una {alimento}")
for alimento in alimentos:
    # ponemos una condición la cual si se cumple se cancela el bucle
    if alimento == "banana":
        break # cancela el bucle que se está ejecutando
    print(f"me como una {alimento}")