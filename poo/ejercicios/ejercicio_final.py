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


class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if -0.8 < polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif -0.3 < polaridad < -0.1:
            return "\x1b[1;31m" + "Algo negativo" + "\x1b[0;37m"
        elif -0.1 <= polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif 0.1 <= polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[0;37m"
        elif 0.4 < polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Muy negativo" + "\x1b[0;37m"


analizador = AnalizadorDeSentimientos()

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
