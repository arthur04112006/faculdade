tupla1 = (1, 2, 3, 4, 5)
tupla2 =(6, 7, 8, 9, 10)
print(f"Tupla 1: {tupla1}")
print(f"Tupla 2: {tupla2}")
position = int(input("digite a posição do elemento que deseja acessar na tupla 1: "))
print(tupla1[position])
concatenar = input("quer concatenar tuplas? s/n: ")
if concatenar.lower() == "sim":
    print(tupla1 + tupla2)
    convert = input("deseja converter a tupla em lista? s/n: ")
    if convert.lower() == "sim":
        lista = list(tupla1 + tupla2)
        print(lista)
        desconverter = input("deseja desconverter a lista em tupla? s/n: ")
        if desconverter.lower() == "sim":
            print(tupla1 + tupla2)
        else:
            print("lista não convertida")
    else:
        print("tupla não convertida")
else:
    print("tupla não concatenada")
    
