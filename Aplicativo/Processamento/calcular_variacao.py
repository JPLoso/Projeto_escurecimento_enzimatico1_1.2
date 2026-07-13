def calcular_variacao(resultados):
    """
    Calcula a variação percentual dos pixels escuros e claros
    entre imagens consecutivas.

    resultados:
    {
        "T1": {"escuras": 5.9, "claras": 94.1},
        "T2": {"escuras": 13.4, "claras": 86.6},
        ...
    }
    """

    itens = list(resultados.items())

    variacoes = []

    for i in range(1, len(itens)):
        nome_ant, dados_ant = itens[i - 1]
        nome_atual, dados_atual = itens[i]

        escuros_ant = dados_ant["escuras"]
        escuros_atual = dados_atual["escuras"]

        claros_ant = dados_ant["claras"]
        claros_atual = dados_atual["claras"]

        # evita divisão por zero
        var_escuros = 0 if escuros_ant == 0 else (
            (escuros_atual - escuros_ant) / escuros_ant
        ) * 100

        var_claros = 0 if claros_ant == 0 else (
            (claros_atual - claros_ant) / claros_ant
        ) * 100

        variacoes.append({
            "comparacao": f"{nome_ant} → {nome_atual}",
            "escuros": var_escuros,
            "claros": var_claros
        })

    return variacoes