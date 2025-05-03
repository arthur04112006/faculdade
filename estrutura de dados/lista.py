print ("adicionando na lista")
lista = [1, 2, 3, 4, 5]
print(lista)
dado = int(input("digite o valor para adicionar no inicio da lista: "))
lista.insert(0, dado)
print(lista)
dadoEnd = int(input("digite o valor para adicionar no final da lista: "))
lista.append(dadoEnd)
print(lista)