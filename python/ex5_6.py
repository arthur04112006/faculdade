import math

# cabeçalho
print("-" * 39)
print("CÁLCULO DE DESVIO PADRÃO E VARIÂNCIA (SIMPLIFICADO)")
print("-" * 39)

# entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# calculo de média
media = (n1 + n2 + n3) / 3

# desvio padrao
desvio1 = (n1 - media) ** 2
desvio2 = (n2 - media) ** 2
desvio3 = (n3 - media) ** 2

# variância
variancia = (desvio1 + desvio2 + desvio3) / 3

# desvio padrao
desvio_padrao = math.sqrt(variancia)

# exibindo dados
print(f"\nMédia: {media:.2f}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")

#--------------------------------------------------------------------
#exercicio 7
#cabecalho
print("-"*39)
print("CÁLCULO DE MODA (SIMPLIFICADO)")
print("-"*39)

#entrada de dados
n2 = int(input("Digite qualquer número: "))
n1 = int(input("Digite qualquer número: "))
n3 = int(input("Digite qualquer número: "))
n4 = int(input("Digite qualquer número: "))
n5 = int(input("Digite qualquer número: "))
n6 = int(input("Digite qualquer número: "))

numeros = [n1, n2, n3, n4, n5, n6]
repetidos = []

for num in numeros:
    if numeros.count(num) > 1 and num not in repetidos:
        repetidos.append(num)

#logica de moda
if repetidos:
    print(f"os valores repetidos são: {repetidos}")
else: 
    print(f"nâo há valores repetidos")
