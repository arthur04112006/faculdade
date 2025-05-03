numero = int(input("Digite um numero: "))
print(f"Tabuada do {numero}")
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for multiplicador in lista:
#     resultado = numero * multiplicador
#     print(f"{numero} x {multiplicador} = {resultado}")

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")