# lambda funciona de la siguiente manera, lambda "parametros" : "expresion"

variable = list(range(1,11))
es_verdadero = list(filter(lambda x: x%2 == 0, variable))

print(es_verdadero)

