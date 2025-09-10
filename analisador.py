def analisar_texto(texto):
    # Contar palavras
    palavras = texto.split()
    num_palavras = len(palavras)
    
    # Contar caracteres
    num_caracteres = len(texto)
    
    # Contar frases (supondo que terminam com . ! ?)
    frases = texto.split('.') + texto.split('!') + texto.split('?')
    num_frases = len([f for f in frases if f.strip()])
    
    # Palavra mais frequente
    contagem = {}
    for palavra in palavras:
        palavra = palavra.lower().strip('.,!?;:')
        if palavra:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    
    palavra_mais_frequente = max(contagem, key=contagem.get) if contagem else "Nenhuma"
    
    return {
        'palavras': num_palavras,
        'caracteres': num_caracteres,
        'frases': num_frases,
        'palavra_mais_frequente': palavra_mais_frequente,
        'frequencia': contagem.get(palavra_mais_frequente, 0)
    }

# Exemplo de uso
if __name__ == "__main__":
    texto = "Olá mundo! Como vocês estão? Espero que estejam bem. Tenham todos um ótimo dia!"
    resultado = analisar_texto(texto)
    
    print(f"Palavras: {resultado['palavras']}")
    print(f"Caracteres: {resultado['caracteres']}")
    print(f"Frases: {resultado['frases']}")
    print(f"Palavra mais frequente: '{resultado['palavra_mais_frequente']}' ({resultado['frequencia']} vezes)")