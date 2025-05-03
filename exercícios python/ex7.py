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
if repetidos:#verifica se a lista repetidos recebeu algum numero da logica, caso renha recebido é imprimida, caso não, nao é imprimida
    print(f"os valores repetidos são: {repetidos}")
else: 
    print(f"nâo há valores repetidos")