# devolver la secuencia de fibonacci

def fibonacci(desde):
    a, b = desde, desde + 1
    while True:
        yield a
        a, b = b, a+b

secuencia = fibonacci(1)

for _ in range(100):
    print(next(secuencia), end=', ')