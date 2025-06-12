def soma_naturais_rec(n: int) -> int:
    if n ==1:
        return 1
    return n + soma_naturais_rec(n - 1)

print(soma_naturais_rec(5))  # Deve imprimir 15 (1 + 2 + 3 + 4 + 5)