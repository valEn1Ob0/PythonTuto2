import re

email = "example@example.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resultado = re.match(pattern,email) # busca la expresión en el texto seleccionado

if resultado:
    print("Email valido")
else:
    print("Email invalido")