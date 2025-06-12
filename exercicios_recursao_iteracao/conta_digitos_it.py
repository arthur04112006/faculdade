def contar_digitos_it(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 1
    contador = 0
    while n > 0:
        n //= 10
        contador += 1
    return contador
print(contar_digitos_it(17172653))  # Deve imprimir 8 (1, 7, 1, 7, 2, 6, 5, 3)