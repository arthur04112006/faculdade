def hanoi_it(n: int, origem: str, destino: str, auxiliar: str) -> list:
    movimentos = []
    total_movimentos = 2**n - 1

    if n % 2 == 0:
        destino, auxiliar = auxiliar, destino  # troca destino e auxiliar se par

    torres = {
        origem: list(range(n, 0, -1)),
        destino: [],
        auxiliar: []
    }

    def mover_de_para(a, b):
        if not torres[a]:
            disco = torres[b].pop()
            torres[a].append(disco)
            movimentos.append(f"Mover disco {disco} de {b} para {a}")
        elif not torres[b]:
            disco = torres[a].pop()
            torres[b].append(disco)
            movimentos.append(f"Mover disco {disco} de {a} para {b}")
        elif torres[a][-1] < torres[b][-1]:
            disco = torres[a].pop()
            torres[b].append(disco)
            movimentos.append(f"Mover disco {disco} de {a} para {b}")
        else:
            disco = torres[b].pop()
            torres[a].append(disco)
            movimentos.append(f"Mover disco {disco} de {b} para {a}")

    for i in range(1, total_movimentos + 1):
        if i % 3 == 1:
            mover_de_para(origem, destino)
        elif i % 3 == 2:
            mover_de_para(origem, auxiliar)
        else:
            mover_de_para(auxiliar, destino)

    return movimentos
