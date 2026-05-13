import numpy as np

def calc_percentuais(region_mask, region_gray):

    # Seleciona apenas pixels válidos
    pixels_validos = region_gray[region_mask > 0]

    # Caso não existam pixels válidos
    if len(pixels_validos) == 0:
        return (0, 0)

    # Pixels escuros
    escuros = np.sum(pixels_validos <= 127)

    # Pixels claros
    claros = np.sum(pixels_validos > 127)

    # Total de pixels
    total = len(pixels_validos)

    # Retorna percentuais
    return (
        escuros / total * 100,
        claros / total * 100
    )