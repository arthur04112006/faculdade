def soma_naturais_it(n: int) -> int:
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma
print(soma_naturais_it(5))  # Deve imprimir 15 (1 + 2 + 3 + 4 + 5)