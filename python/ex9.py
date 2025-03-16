from datetime import datetime

nome = input("Qual seu nome? ")
data_nasc_informada =  input("Qual a data do seu nascimento? (dia/mês/ano): ")
cidade = input("Qual a cidade onde você nasceu? ")

data_nasc = datetime.strptime(data_nasc_informada, "%d/%m/%Y")

hoje = datetime.today()
idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

print(f"{nome}, você tem {idade} anos e nasceu em {cidade}.")



