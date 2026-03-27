#Importação da função interna e do responsavel por analise de imagens
from Aplicativo.Processamento.calc_percentual import calc_percentuais
import cv2

#Define a função analisar imagem
def analisar_imagem(img, mask):
    #Converte as cores da imagme em tons de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return calc_percentuais(mask, gray)