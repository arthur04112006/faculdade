print("-"*16)
print("Cálculo da média")
print("-"*16)

recebimento_numeros = input("Digite os numeros separados por espaço: ")
numeros = list(map(int, recebimento_numeros.split()))#slipt divide a string em substrings
#a função map aplica a função int a cada elemento da lista resultante do split


def calcular_media(numeros):
    return sum(numeros) / len(numeros)

media = calcular_media(numeros)
print(f"A média dos numeros é: {media:.2f}")