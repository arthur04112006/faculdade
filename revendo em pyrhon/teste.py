import csv

with open('teste.csv', encoding='utf-8') as file:
    dados = list(csv.DictReader(f))
    maiores = [p["nome"] for p in dados if int(p["idade"]) >= 18]

print(dados)