# Operadores bit a bit en acción

# Declaramos dos números enteros
a = 5  # En binario: 0101
b = 3  # En binario: 0011

# AND bit a bit (&)
and_result = a & b  # Comparación bit a bit: 0101 & 0011 = 0001
print(f"AND bit a bit: {a} & {b} = {and_result}")  # Resultado: 1

# OR bit a bit (|)
or_result = a | b  # Comparación bit a bit: 0101 | 0011 = 0111
print(f"OR bit a bit: {a} | {b} = {or_result}")  # Resultado: 7

# XOR bit a bit (^)
xor_result = a ^ b  # Comparación bit a bit: 0101 ^ 0011 = 0110
print(f"XOR bit a bit: {a} ^ {b} = {xor_result}")  # Resultado: 6

# NOT bit a bit (~)
not_a = ~a  # Invierte los bits: ~0101 = -(0101 + 1) = -6
print(f"NOT bit a bit: ~{a} = {not_a}")  # Resultado: -6

# Desplazamiento a la izquierda (<<)
left_shift = a << 1  # Desplaza los bits de a una posición a la izquierda: 0101 << 1 = 1010
print(f"Desplazamiento a la izquierda: {a} << 1 = {left_shift}")  # Resultado: 10

# Desplazamiento a la derecha (>>)
right_shift = a >> 1  # Desplaza los bits de a una posición a la derecha: 0101 >> 1 = 0010
print(f"Desplazamiento a la derecha: {a} >> 1 = {right_shift}")  # Resultado: 2
