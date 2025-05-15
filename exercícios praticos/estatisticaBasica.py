import statistics

def estatistica3M(recebeDado):  
    m = statistics.mean(recebeDado)
    m1 = min(recebeDado)
    m2 = max(recebeDado)
    exibicao = (f"media: {m}, minimo : {m1}, maximo: {m2}")
    print(exibicao)


dados = (2, 5, 8, 12, 31, 1, 9, 10)

estatistica3M(dados)