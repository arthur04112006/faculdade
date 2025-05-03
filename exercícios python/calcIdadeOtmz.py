from datetime import date

# Cabeçalho
print('=' * 16)
print('CÁLCULO DE IDADE')
print('=' * 16)

# Entrada de dados
nome = input('Digite seu nome: ')
dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))

# Processamento e cálculo da idade
data_nasc = date(ano, mes, dia)
hoje = date.today()

idade = hoje.year - data_nasc.year

# Ajusta caso ainda não tenha feito aniversário este ano
if (mes, dia) > (hoje.month, hoje.day):
    idade -= 1

# Saída
print(f'{nome} tem {idade} anos.')
