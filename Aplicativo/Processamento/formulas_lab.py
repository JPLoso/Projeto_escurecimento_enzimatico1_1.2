def calcular_ie(L, a, b):
    x = (a + 1.75 * L) / (5.645 * L + a - 3.021 * b)
    return (100 * (x - 0.31)) / 0.172

def calc_perc_ie(ie_inicial, ie_final):
    if ie_inicial == 0:
        return 0
    esc = ((ie_final - ie_inicial)/ie_inicial) * 100
    return esc


def calcular_variacao_ie(resultados):
    itens = list(resultados.items())
    ie0 = itens[0][1]["ie"]
    variacoes = []

    for nome, dados in itens:
        if ie0 == 0:
            perc = 0
        else:
            perc = ((dados["ie"]-ie0)/ie0)*100

        variacoes.append({
            "imagem":nome,
            "ie":dados["ie"],
            "variacao":perc
        })

    return variacoes