# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
    

# print(fatorial(6))

# numero = int(input("Digite um número para calcular o fatorial: "))
# resultado = fatorial(numero)
# print(f"O fatorial de {numero} é {resultado}")

#########################################

# def contagem(n):
#     if n == 0:
#         print("fogo")
#     else:
#         print(n)
#         contagem(n - 1)
# contagem(10)

##########################################

# def tabuada_recursivan(n, multiplicador=1):
#     if multiplicador > 10:
#         return
#     print(f"{n} x {multiplicador} = {n * multiplicador}")
#     tabuada_recursivan(n, multiplicador + 1)

# tabuada_recursivan(5)

# Exemplo de uso

###########################################

def tabuada_iterativa(n):
    for i in range(10):
        print(f"{n} x {i+1} = {n * (i + 1)}")

tabuada_iterativa(5)