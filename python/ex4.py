#cabecalho
print("-"*26)
print("CÁLCULO DE MÉDIA PONDERADA")
print("-"*26)

#variaveis notas
n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))
n3 = float(input("Digite a nota da terceira prova: "))

#variaveis pesos
p1 = float(input("Digite o peso da primeira prova: "))
p2 = float(input("Digite o peso da segunda prova: "))
p3 = float(input("Digite o peso da terceira prova: "))

#logica
media_ponderada = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

#exibição dos dados
print(f"A média ponderada das notas é: {media_ponderada:.2f}")
