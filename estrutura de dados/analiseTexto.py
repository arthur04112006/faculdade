def frequencia(texto):
    palavras = texto.split()
    freq = {}
    
    for palavra in palavras:
        palavra = palavra.lower().strip('.,!?;:"()') 
        if palavra:
            if palavra in freq:
                freq[palavra] += 1
            else:
                freq[palavra] = 1
    return freq

def estatisticas(texto):
    freq = frequencia(texto)
    
    if not freq:
        return (0, 0, (None, 0))
    
    total_palavras = sum(freq.values())
    palavras_unicas = len(freq)
    mais_comum = max(freq.items(), key=lambda x: x[1])
    
    return (total_palavras, palavras_unicas, mais_comum)

def mostrar_resultados(texto):
    print("\n=== RESULTADOS DA ANÁLISE ===")
    
    freq_dict = frequencia(texto)
    
    print("\n1. Frequência de cada palavra:")
    for palavra, count in freq_dict.items():
        print(f"'{palavra}': {count} vez(es)")

    stats = estatisticas(texto)
    print("\n2. Estatísticas gerais:")
    print(f"- Total de palavras: {stats[0]}")
    print(f"- Palavras únicas: {stats[1]}")
    print(f"- Palavra mais comum: '{stats[2][0]}' ({stats[2][1]} ocorrências)")

    if freq_dict:
        mais_freq = max(freq_dict.items(), key=lambda x: x[1])
        menos_freq = min(freq_dict.items(), key=lambda x: x[1])
        print("\n3. Extremos de frequência:")
        print(f"- Palavra mais frequente: '{mais_freq[0]}' ({mais_freq[1]} vezes)")
        print(f"- Palavra menos frequente: '{menos_freq[0]}' ({menos_freq[1]} vez)")
    try:
        n = int(input("\n4. Digite um número N para ver palavras que aparecem mais que N vezes: "))
        palavras_freq = [p for p, c in freq_dict.items() if c > n]
        if palavras_freq:
            print(f"Palavras com mais de {n} ocorrências: {', '.join(palavras_freq)}")
        else:
            print(f"Nenhuma palavra aparece mais que {n} vez(es)")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

def main():
    """Função principal do programa"""
    print("=== ANALISADOR DE TEXTO ===")
    print("Digite o texto que deseja analisar e pressione Enter:")
    print("(Pode ser uma frase, parágrafo ou até um texto longo)\n")

    texto_usuario = input(">> ")
    
    if not texto_usuario.strip():
        print("\nPor favor, digite algum texto para analisar.")
        return
    mostrar_resultados(texto_usuario)

if __name__ == "__main__":
    main()