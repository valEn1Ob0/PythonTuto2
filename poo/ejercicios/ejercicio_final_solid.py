import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = """hace de cuenta que sos una analizador de sentimientos. 
Yo te paso sentimientos y vos analizas de los mensajes
y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
SOLO RESPUESTAS NUMÉRICAS. Donde -1 es negatividad maxima y 1 es positividad maxima,
el rango funciona asi:
menos o igual a -0.8 es muy negativo, entre -0.8 y -0.3 es negativo,
entre -0.3 y -0.1 es algo negativo, entre -0.1 y 0.1 es neutral,
entre 0.1 y 0.4 es algo positivo, entre 0.4 y 0.9 es positivo
y mayor a 0.9 es muy positivo.
(Podes solo responder SOLO con enteros o flotantes)"""

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)


class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")


rangos = [
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Algo negativo", "31")),
    ((-0.1, 0.1), Sentimiento("Neutral", "33")),
    ((0.1, 0.4), Sentimiento("Algo positivo", "32")),
    ((0.4, 0.9), Sentimiento("Positivo", "32")),
    ((0.9, 1), Sentimiento("Muy positivo", "32"))
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = str(input("\x1b[1;33m" + "Prompt: "))
    if user_prompt == "exit":
        exit(0)

    respuesta = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt),
        contents=user_prompt
    )

    valor = float(respuesta.text.strip())
    sentimiento = analizador.analizar_sentimiento(valor)
    print(sentimiento)
