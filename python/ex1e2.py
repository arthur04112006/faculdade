#cabeçalho
print("-"*21)
print("CRIAÇÃO DE PERSONAGEM ")
print("-"*21)

#variaveis
nome = input("Digite o nome do super-herói: ")
idade = int(input("Digite sua idade: "))
poder_especial = input("Digite seu poder especial: ")
nivel_energia = int(input("Digite seu nivel de energia de 0 a 100: "))
missao = input("esta em missao (sim/não): ")


#exibição de dados
print("-"*19)
print("FICHA DO PERSONAGEM")
print("-"*19)
print("Nome: ", nome)
print(f"Idade: {idade} anos")
print("Poder especial: ", poder_especial)
print(f"Nivel de energia: {nivel_energia} %")
print("Em missao: ", missao)

#etapa 2 - poder personagem

print("-"*29)
print("NÍVEL DE PODER DO PERSONAGEM")
print("-"*29)

#declaração das variaveis etapa 2 
forca = int(input("Digite a força do personagem de 1 a 10: "))
agilidade = int(input("Digite a agilidade do personagem de 1 a 10: "))
inteligencia = int(input("Digite a inteligencia do personagem de 1 a 10: "))
poder = (forca + agilidade + inteligencia) 

print("-"*25)
print("-"*25)
print("Poder do personagem: ", poder)
print("-"*25)
print("-"*25)

print("-"*18)
print("FIM DO PROGRAMA ;)")
print("-"*18)
