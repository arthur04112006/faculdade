dados = input("digite os numeros separados por espaço:")
numeros = list(map(int, dados.split()))
soma = 0

for numero in numeros:
    soma += numero 
print (soma)


