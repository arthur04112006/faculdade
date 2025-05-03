#cabecalho
print("-"*25)
print("CÁLCULO DE MÉDIA DE NOTAS")
print("-"*25)

#variaveis
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
#calculo da media
media = (n1 + n2 + n3) / 3

print("-"*19)
print("RESULTADO DA MÉDIA")
print("-"*19)

#exibição de dados
print(f"sua média é {media:.2f}")

print("Sera que você passou?")
if media >= 7:
    print("Sim, parabéns, você foi aprovado")
elif media >= 5:
    print("Não, você está de recuperação final, se esforçe mais")
else:
    print("Infelizmente você foi reprovado")



