palavraFornecida = input("Digite uma palavra para ver se ela é palidromo: ")
palavraConvertida = palavraFornecida[::-1]

if palavraFornecida == palavraConvertida:
    print(f"é palidromo, {palavraConvertida}")
else: 
    print(f"não é palidromo {palavraFornecida} / {palavraConvertida}")