nombres: list[str] = ["n1","n2","n3"]
apellidos: list[str] = ["a1","a2","a3"]

with open("nombres.txt","w") as f:
    f.writelines("Los datos son:\n\n")
    f.writelines(f"nombre: {n}\napellido: {a}\n--------\n" for n, a in zip(nombres,apellidos))