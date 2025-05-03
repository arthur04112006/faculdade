#bibliotecas
import datetime 
from datetime import date
#cabecalho
print ('='*20)
print ('VERIFICADOR DE IDADE')
print ('='*20)
#entrada de dados
nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
idade_informada = int(input('Digite sua idade: '))
cpf = input('Digite seu CPF (apenas números): ')

# processamento de dados
data_nasc = datetime.date(ano, mes, dia)
hoje = date.today()

# calculo da idade real com base na data de nascimento
idade_calculada = hoje.year - data_nasc.year

# ajusta caso a pessoa ainda não tenha feito aniversário este ano
if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
    idade_calculada -= 1

# idade real
print ('='*23)
print(f'//{nome} tem {idade_calculada} anos.\\\\')
print ('='*29)

# verificação da idade informada x idade calculada
if idade_informada == idade_calculada:
    print('Idade informada esta correta.')
else:
    print(f'Idade informada esta incorreta:{idade_informada} anos. Idade real: {idade_calculada} anos.')
print ('='*29)
print ('Aqui estão seus dados:')
print ('NOME:', nome)
print ('EMAIL:', email)
print ('CPF:', cpf)
print ('IDADE REAL:', idade_calculada)
print ('IDADE INFORMADA:', idade_informada)
print ('='*20)


# codigo abaixo é um codigo de teste reaproveitado e desenvolvido a mao, porem a logica nao funcionou e foi trocada pela logica acima



#processamento dos dados
# dataNasc = datetime.date(ano, mes, dia)
# diferenca = date.today() - dataNasc
# #calculos e resultados
# result = (diferenca.days / 365.25)
# #formata string, onde %d torna o número inteiro/exibição de dados
# resultado = ('%s tem %d anos.' % (nome, result))
# print(resultado)
# #exibição de dados
# if idade == diferenca:
#     print('Idade informada correta')
# else:
#     print('Idade informada incorreta')
