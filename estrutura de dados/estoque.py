estoque = {
    "uva": "5",
    "banana": "3",
    "laranja": "10",
    "maçã": "8",
    "morango": "3",
    "abacaxi": "4",
    "mamão": "7",
    "melancia": "2",
    "limão": "15",
    "pera": "9",
    "manga": "5"
}
decisao = input("""1- adicionar produtos
2- alterar quantidades
3- remover produtos
4- disponibilidade
5- relatorio de baixo estoque
Oque deseja fazer? """)
if decisao == "1":
    print(estoque)
    produto = input("adicionar produto: ")
    quantidade = input("digite a quantidade: ")
    estoque[produto] = quantidade
    print(estoque)
elif decisao == "2":
    print(estoque)
    produto = input("qual produto quer alterar quantidade? ")
    quantidade = input("digite a quantidade: ")
    estoque[produto] = quantidade
    print(estoque)
elif decisao == "3":
    print(estoque)
    produto = input("qual produto remover? ")
    estoque.pop(produto)
    print(estoque)
elif decisao == "4": 
    print(estoque.keys())
    produto = input("qual produto deseja ver as quantidades? ")
    print(f"quantidade de {produto}: {estoque[produto]}")
elif decisao == "5":
    itens_baixo_estoque = {p: q for p, q in estoque.items() if int(q) <= 5}
    if itens_baixo_estoque:
        print("itens com estoque baixo:")
        for produto, quantidade in itens_baixo_estoque.items():
            print(f"{produto}: {quantidade}")
    else:
        print("nenhum item com estoque baixo")
else: 
    print("Erro! numero incorreto")

# estoque = {}
# produto = input("adicionar produto: ")
# quantidade = input("digite a quantidade: ")
# estoque[produto] = quantidade
# print(estoque)