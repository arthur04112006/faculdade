numero = int(input("Digite o numero para ver a tabuada: "))
for i in range(1,11):
    if i % 2 == 0:
        print (f"{numero} X {i} = {numero * i}") 
