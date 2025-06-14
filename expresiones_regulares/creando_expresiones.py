import re

text = "Hola pedro mi numero es: +54 11 1234-5555"
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

remplazo = re.sub(pattern,"(Numero oculto)",text)

print(remplazo)