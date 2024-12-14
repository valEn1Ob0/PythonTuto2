otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curos = 1.5

# duración de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duración
def cursos(curso):
    return 100 - dalto_curos * 1000 // curso / 10
diferencias_con_min = cursos(otros_cursos_min)
diferencias_con_max = cursos(otros_cursos_max)
diferencias_con_promedio = cursos(otros_cursos_promedio)

# tiempo crudo removido
tiempo_vacio_removido = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_removido_dalto = 100 - dalto_curos * 1000 // crudo_dalto / 10

print('................')
print(f"el curso de dalto dura un {diferencias_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencias_con_max}% menos que el mas lento")
print(f"el curso de dalto dura un {diferencias_con_promedio}% menos que el promedio de cursos")
print('................')


print(f"el tiempo vacio promedio fue de {tiempo_vacio_removido}")
print(f"el tiempo vacio promedio de dalto fue de {tiempo_vacio_removido_dalto}")
print('................')

# diferencias si los cursos duraran 10hs

print(f"ver 10 horas de este curso equivale ver {otros_cursos_promedio * 100 // dalto_curos / 10} horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale ver {dalto_curos * 100 // otros_cursos_promedio / 10} horas de cursos de dalto")
print('................')