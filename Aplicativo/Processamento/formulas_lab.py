def calcular_ie(L, a, b):
    x = (a + 1.75 * L) / (5.645 * L + a - 3.021 * b)
    return (100 * (x - 0.31)) / 0.172

def calc_perc_ie(ie_inicial, ie_final):
    if ie_inicial == 0:
        return 0
    esc = ((ie_final - ie_inicial)/ie_inicial) * 100
    return esc