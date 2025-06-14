import re

email = "example@example.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resutl = re.match(pattern,email) # busca la expresion en el texto seleccionado

if resutl:
    print("Email valido")
else:
    print("Email invalido")