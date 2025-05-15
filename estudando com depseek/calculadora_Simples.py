print("="*32)
print("Bem vindo a Calculadora Simples! ")
print("="*32)

decisao = int(input(f"""Selecione a operacao:
1 - soma
2 - subtração
3 - multiplicação
4 - divisão
5 - todas acima
: """))

valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
if valor2 != 0:
    divisao = valor1 / valor2
else: 
   divisao = "Divisão por zero impossível!"

if decisao == 1:
    print(f"A soma dos valores é {soma}")
elif decisao == 2:
    print(f"A subtração dos valores é {subtracao}")
elif decisao == 3:
    print(f"A multiplicação dos valores é {multiplicacao}")
elif decisao == 4:
    print(f"A divisão dos valores é {divisao}")
elif decisao == 5:
    print("*"*18)
    print("Resultados Abaixo: ")
    print("*"*18)
    print(f"""Soma: {soma}
Subtração: {subtracao}
Multiplicação: {multiplicacao}
Divisão: {divisao}


Fim!!!


""")
    

