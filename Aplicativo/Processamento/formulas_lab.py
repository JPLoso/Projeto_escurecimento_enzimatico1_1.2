def ie(x):
    ie = (100 * (x - 0.31)) / 0.172
    return ie  

def valor_X(a):
    x = (a + 1.75) / (5.645 + a - 3.021)
    return x

def calc_perc_ie(ie_inicial, ie_final):
    esc = ((ie_final - ie_inicial)/ie_inicial) * 100
    return esc