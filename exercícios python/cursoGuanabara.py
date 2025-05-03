# Desafio 1

print('desafio 1')

nome = input('Qual seu nome?')
sobrenome = input('Qual seu sobrenome?')
ultimoNome = input('Qual seu último nome?')

print(f'Você é {nome} {sobrenome} {ultimoNome}')

#desafio 2

print('Desafio 2')

dia = input('Qual o dia do seu nascimento?')
mes = input('Qual o mês do seu nascimento?')
ano = input('Qual o ano do seu nascimento?')

print(f'Você nasceu no dia {dia} de {mes} de {ano}. Correto?')
if input('') == 'sim':
    print('Obrigado por confirmar!')
else:
    print('Por favor, informe novamente.')

#desafio 3

print('Desafio 3')
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é {soma}')