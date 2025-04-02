dados = input("digite os numeros separados por espaço:")
lista = list(map(int, dados.split()))  # split divide a string em substrings
soma = 0
peso = 0

for z in lista:
    soma += z
    peso += 1

media = soma / peso if peso != 0 else 0
print(f"Média: {media:.2f}")







# print(f"numeros: {numeros}")