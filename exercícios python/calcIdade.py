import datetime
from datetime import date

#cabecalho
print ('='*16)
print ('CÁLCULO DE IDADE')
print ('='*16)

#entrada de dados
nome = input('Digite seu nome: ')
dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))

#processamento dos dados
dataNasc = datetime.date(ano, mes, dia)
diferenca = date.today() - dataNasc

#calculos e resultados 
result = (diferenca.days / 365.25)

#formata string, onde %d torna o número inteiro 
print ('%s tem %d anos.' % (nome, result))




