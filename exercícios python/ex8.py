

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print(f"nome: {nome}")
print(f"Idade: {idade}")
print(f"altura: {altura}M")

if idade <= 18:
    print("você é menor de idade")
elif idade <= 65:
    print("você é adulto")
else:
    print("você é idoso")