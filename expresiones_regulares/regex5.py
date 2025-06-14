import re

text = "Este es un ejemplo de una pagina web: https://www.ejemplo.com"
pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)