#Importações
import numpy as np

#Definição da função
def calc_percentuais(region_mask, region_gray):
    #Guarda o numero de pixels que não sejam completamente pretor
    pixels_validos = region_gray[region_mask > 0]

    #Para caso não houver numero de pixeis validos
    if len(pixels_validos) == 0:
        return (0, 0, 0)
    
    #Define o padrão de cores para o calculo
    escuros = np.sum(pixels_validos <= 85)
    medios = np.sum((pixels_validos > 85) & (pixels_validos <= 170))
    claros = np.sum(pixels_validos > 170)

    #Armazena quantidade de pixeis calculados
    total = len(pixels_validos)

    #Realiza o calculo dos pixels
    return (
        escuros / total * 100,
        medios / total * 100,
        claros / total * 100
    )