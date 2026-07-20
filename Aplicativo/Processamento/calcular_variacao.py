def calcular_variacao(resultados):
    """
    Calcula a variação percentual dos pixels escuros e claros
    em relação à primeira imagem (tempo inicial).
    """

    itens = list(resultados.items())

    if not itens:
        return []

    escuros0 = itens[0][1]["escuras"]
    claros0 = itens[0][1]["claras"]

    variacoes = []

    for nome, dados in itens:
        escuros = dados["escuras"]
        claros = dados["claras"]

        var_escuros = 0 if escuros0 == 0 else (
            (escuros - escuros0) / escuros0
        ) * 100

        var_claros = 0 if claros0 == 0 else (
            (claros - claros0) / claros0
        ) * 100

        variacoes.append({
            # Mantém a chave esperada pelo restante do programa
            "comparacao": nome,
            "escuros": var_escuros,
            "claros": var_claros
        })

    return variacoes