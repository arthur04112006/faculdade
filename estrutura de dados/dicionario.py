
listaTelefonica = {
    "andre": "(45)12345-6789",
    "lucas": "(45)98765-4321",
    "maria": "(45)11111-2222",
    "joao": "(45)22222-3333",
    "jose": "(45)44444-5555",
    "ana": "(45)66666-7777",
    "carla": "(45)88888-9999",
    "paulo": "(45)00000-1111",
    "felipe": "(45)22222-4444",
    "rafael": "(45)33333-5555",
}
print("lista telefonica: ")
for chave in listaTelefonica:
    exibicao = (f"{chave}: {listaTelefonica[chave]}")
    print(exibicao)
decisao = int(input("oque deseja fazer? 1 - adicionar, 2 - pesquisar, 3 - remover: "))
if decisao == 1:
    contatoAdd = input("digite o nome e contato para adicionar: ex: joao (44)9999-9999  ")
    contatoAdd = contatoAdd.split(" ")
    listaTelefonica[contatoAdd[0]] = contatoAdd[1]
    exibicao = (f"{chave}: {listaTelefonica[chave]}")
    print(exibicao)
elif decisao == 2:
    pesquisa = input("qual nome quer pesquisar? : ")
    if pesquisa in listaTelefonica:
        novo = {}
        novo[pesquisa] = listaTelefonica[pesquisa]
        print(f"o contato existe: {novo}")
        novo.pop(pesquisa)
elif decisao == 3: 
    pesquisa = input("qual nome quer remover? : ")
    if pesquisa in listaTelefonica: 
        listaTelefonica.pop(pesquisa)
        for chave in listaTelefonica:
            exibicao = (f"{chave}: {listaTelefonica[chave]}")
            print(exibicao)
        print("=" *15)
        print(f"contato {pesquisa} removido!")
        print("=" *15)
    else: 
        print("contato nao encontrado")
else:
    print("erro")
    




