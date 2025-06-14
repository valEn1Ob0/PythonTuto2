import re

text = "remplazando vocales por asterisco"

new_text = re.sub("[aeiou]", "*", text)

print(new_text)