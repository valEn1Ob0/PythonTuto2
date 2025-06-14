import re

text = "fechas: 23/01/2020, y el telefono es: +1-555-555-5555"

pattern = r"\d{2}/\d{2}/\d{4}"

remplazo = "Fecha oculta"

nuevo_texto = re.sub(pattern,remplazo,text) # el re.sub lo que hace es usar el patron con el remplazo para remplazar el texto  

print("Texto modificado", nuevo_texto)