import math

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.sqrt(n)
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True

def generar_primos(hasta):
    return [n for n in range(2, hasta+1) if es_primo(n)]

print('Iniciando...')
hasta = 30
print(f'Generando números primos hasta {hasta}...')
primos = generar_primos(hasta)
print(f'Los números primos hasta {hasta} son: {primos}')
