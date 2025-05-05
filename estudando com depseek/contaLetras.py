palavra = input("Digite uma palavra ou texto para contar as letras: ")

contador = len(palavra) - palavra.count(" ")
print(f"seu texto tem {contador} letras")