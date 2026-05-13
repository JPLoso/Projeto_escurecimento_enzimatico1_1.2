from Aplicativo.Visualizacao.plotar_grafico import plotar_grafico

from Aplicativo.Processamento.analisar_imagem import analisar_imagem
from Aplicativo.Processamento.criar_mascara import criar_mascara
from Aplicativo.Processamento.carregar_imagem import carregar_imagem

def gerar_grafico(caminho):

    img = carregar_imagem(caminho)

    mask = criar_mascara(img)

    valores = analisar_imagem(img, mask)

    plotar_grafico(valores)

    return valores