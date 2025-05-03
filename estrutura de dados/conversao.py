lista_tuplas = [("a", 1), ("b", 2)]
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}
lista_itens = ["a", "b", "a", "c", "b", "a"]

resultado1 = dict(lista_tuplas)
print("1. Lista de tuplas para dicionário:")
print(f"{lista_tuplas} = {resultado1}\n")

resultado2 = list(dicionario1.items())
print("2. Dicionário para lista de tuplas:")
print(f"{dicionario1} = {resultado2}\n")

resultado3 = {}
for item in lista_itens:
    if item in resultado3:
        resultado3[item] += 1
    else:
        resultado3[item] = 1
print("3. Lista para dicionário de contagem:")
print(f"{lista_itens} = {resultado3}\n")

resultado4 = dicionario1.copy()
for chave, valor in dicionario2.items():
    if chave in resultado4:
        resultado4[chave] += valor
    else:
        resultado4[chave] = valor
print("4. Combinar dois dicionários:")
print(f"{dicionario1} + {dicionario2} = {resultado4}")