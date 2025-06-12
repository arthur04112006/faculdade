def contar_digitos_rec(n: int) -> int:
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos_rec(n // 10)
print(contar_digitos_rec(12345))  # Deve imprimir 5